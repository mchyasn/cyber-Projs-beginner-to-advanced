chrome.tabs.onUpdated.addListener((tabId, changeInfo, tab) => {
  if (changeInfo.url && changeInfo.url.startsWith("http://")) {
    chrome.notifications.create({
      type: "basic",
      iconUrl: "icons/icon48.png",
      title: "Insecure Site Detected",
      message: "You are visiting a non-HTTPS website. Proceed with caution."
    });
  }
});
