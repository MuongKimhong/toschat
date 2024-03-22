if application "iTerm" is running then
    tell application "iTerm"
        set bounds of current window to {0, 0, 900, 750}
    end tell
end if

if application "iTerm2" is running then
    tell application "iTerm2"
        set bounds of current window to {0, 0, 900, 750}
    end tell
end if

if application "Terminal" is running then
    tell application "Terminal"
        set bounds of current window to {0, 0, 900, 750}
    end tell
end if
