import ltk
import logging
import state
from pyscript import window # type: ignore
import constants

logger = logging.getLogger('root')


def create_menu():
    return ltk.MenuBar(
        ltk.Menu("File",
             ltk.MenuItem("➕", "New", "", lambda item: new_sheet()),
             ltk.MenuItem("📂", "Open", "Cmd+O", lambda item: go_home()),
             ltk.MenuItem("🎁", "Share", "", lambda item: share_sheet()),
             ltk.MenuItem("🗑", "Delete", "", lambda item: delete_doc()),
        ),
        ltk.Menu("Edit",
             ltk.MenuItem("✂️", "Copy", "", lambda: None),
             ltk.MenuItem("📋", "Paste", "", lambda: None),
        ),
        ltk.Menu("View",
             ltk.MenuItem("◱", "Full Screen", "", lambda event: ltk.document.body.requestFullscreen()),
        ),
    )
DELETE_PROMPT = """
This will permanently delete the current sheet.
You and anyone it has been shared with will lose access.
We cannot recover the contents.

Enter the name of the sheet to actually delete it:")
"""


def delete_doc():
    if window.prompt(DELETE_PROMPT) == state.doc.name:
        url = f"/file?{constants.DATA_KEY_UID}={state.doc.uid}"
        ltk.delete(state.add_token(url), lambda data: go_home())


def go_home():
    window.document.location = "/"


def load_doc(uid):
    window.document.location = f"?{constants.DATA_KEY_UID}={uid}"


def share(uid, email):
    logger.info("share %s %s %s", uid, "with", email)
    def confirm(response):
        if response[constants.DATA_KEY_STATUS] == "error":
            logger.error(response[constants.DATA_KEY_STATUS])
            window.alert(response[constants.DATA_KEY_STATUS])
        logger.info(f"Sheet {state.doc.uid} was shared with {email}")

    url = f"/share?{constants.DATA_KEY_UID}={uid}&{constants.DATA_KEY_EMAIL}={email}"
    ltk.get(state.add_token(url), ltk.proxy(confirm))
    close_share_dialog()


def close_share_dialog():
    ltk.find(".share-popup").dialog('close')


def new_sheet():
    state.doc.name = "Untitled"
    ltk.get(state.add_token("/file"), ltk.proxy(lambda data: load_doc(data[constants.DATA_KEY_UID])))


def share_sheet():
    ltk.VBox(
        ltk.Text("Email name to share with:").addClass("share-label"),
        ltk.Input("").attr("id", "share-email").addClass("share-email"),
        ltk.HBox(
            ltk.Button("Cancel", lambda event: close_share_dialog()).addClass("cancel-button"),
            ltk.Button("Share", lambda event: share(state.doc.uid, ltk.find("#share-email").val())).addClass("share-button"),
        ).css("margin-left", "auto")
    ).dialog().addClass("share-popup").parent().width(350)


ltk.find(".logo").on("click", ltk.proxy(lambda event: go_home()))
