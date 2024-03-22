if application "iTerm" is running then
    tell application "iTerm"
        set bounds of front window to {0, 0, 900, 750}
    end tell
else if application "iTerm2" is running then
    tell application "iTerm2"
        set bounds of front window to {0, 0, 900, 750}
    end tell
else if application "Terminal" is running then
    tell application "Terminal"
        set bounds of front window to {0, 0, 900, 750}
    end tell
end if
