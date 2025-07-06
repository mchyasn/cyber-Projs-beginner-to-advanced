# Secure Web Alert – Browser Security Extension
```
Project Goal:
Build a simple browser extension that warns users when visiting 
non-HTTPS websites, helping increase awareness of insecure web traffic.

Target:
- Chrome
- Brave
- Edge (any Chromium-based browser)
```

Step 0: Create Project Folder
```
mkdir SecureExtension && cd SecureExtension
mkdir icons
touch manifest.json background.js README.txt
```

Step 1: Write Manifest File
```
File: manifest.json
```
```
{
  "manifest_version": 3,
  "name": "Secure Web Alert",
  "version": "1.0",
  "description": "Warns the user when visiting a non-HTTPS website.",
  "permissions": ["tabs", "notifications"],
  "background": {
    "service_worker": "background.js"
  },
  "icons": {
    "48": "icons/icon48.png"
  },
  "action": {
    "default_title": "Secure Web Alert"
  }
}
```

Step 2: Write Background Script

File: background.js
```
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
```

Step 3: Add an Icon

Save a 48x48 PNG icon in:
```
SecureExtension/icons/icon48.png

Suggested icon: padlock, warning sign, or any placeholder
```
![Browser Security Extension](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/SecureExtension/screenshots/1.png)


Step 4: Load Extension into Chrome or Brave
```
1. Go to chrome://extensions
2. Enable Developer Mode (top right toggle)
3. Click "Load unpacked"
4. Select your SecureExtension/ directory
```
![Extension Security Scan](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/SecureExtension/screenshots/2.png)

Step 5: Test
```
Visit: http://neverssl.com
Expected: You should receive a browser notification that warns about insecure connection
```
![Extension Threat Detection](https://raw.githubusercontent.com/mchyasn/cyber-Projs-beginner-to-advanced/main/BeginnerProjects/SecureExtension/screenshots/3.png)

Step 6: Optional Ideas
```
- Check certificate validity and warn if expired
- Highlight phishing domains using a local or public blocklist
- Log visit history to non-HTTPS sites
- Redirect HTTP to HTTPS when available

Legal Note:
This extension is for educational and personal security awareness use. Do not collect user data or deploy it in environments without consent.
```


Date: July 6, 2025
