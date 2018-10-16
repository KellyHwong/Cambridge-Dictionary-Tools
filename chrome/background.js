// Filename: background.js
// Created Date: 2018年10月15日23:26:03
// Author: Kelly Hwong

// A generic onclick callback function.
function genericOnClick(info, tab) {
  console.log("selectionText " + info.selectionText);
  console.log("item " + info.menuItemId + " was clicked");
  console.log("info: " + JSON.stringify(info));
  console.log("tab: " + JSON.stringify(tab));
}

// Open looking up url on selection context
function lookUpOnCambridgeOnClick(info, tab) {
  // open url
  var urlHead = "https://dictionary.cambridge.org/dictionary/english-chinese-simplified/";
  var urlToOpen = urlHead + info.selectionText;
  chrome.tabs.create({ url: urlToOpen });
}

// Create one test item for each context type.
var contexts = ["page","selection","link","editable","image","video",
                "audio"];
for (var i = 0; i < contexts.length; i++) {
  var context = contexts[i];
  var title = "Test '" + context + "' menu item";
  if (context == "selection") {
    // Modify here to set the title of the context menu item
    title = "Look up on Cambridge";
    var id = chrome.contextMenus.create({"title": title, "contexts":[context],
                                       "onclick": lookUpOnCambridgeOnClick});
  } else {
    var id = chrome.contextMenus.create({"title": title, "contexts":[context],
                                       "onclick": genericOnClick});
  }
  console.log("'" + context + "' item:" + id);
}
