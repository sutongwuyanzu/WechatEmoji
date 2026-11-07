# WeChat Emoji Sticker Skill

A Codex skill for creating original animated WeChat sticker packs, validating common upload assets, and organizing submission-ready files.

## Install

Copy the `wechat-emoji-sticker` directory into your Codex skills directory, for example:

```text
%USERPROFILE%\.codex\skills\wechat-emoji-sticker\
```

Then invoke `$wechat-emoji-sticker` or ask Codex to create a WeChat sticker pack.

## Validate a pack

Install Pillow (`python -m pip install Pillow`) and run:

```powershell
python .\wechat-emoji-sticker\scripts\validate_pack.py "D:\path\to\pack"
```

The checker reports GIF frame/loop issues and validates common icon, cover, and banner dimensions/size when those optional assets are present. Requirements may change; check the current WeChat Sticker Platform upload form before submission.

## Contents

- `wechat-emoji-sticker/SKILL.md`: skill entrypoint and workflow
- `wechat-emoji-sticker/references/wechat-upload-checklist.md`: point-in-time constraints transcribed from user-provided screenshots
- `wechat-emoji-sticker/scripts/validate_pack.py`: local preflight validator

The finished dog packs remain in the user's local `G:\Codex files\犬类表情包` folder and are not duplicated in this reusable skill repository.
