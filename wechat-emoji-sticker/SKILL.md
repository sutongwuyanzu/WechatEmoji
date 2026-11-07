---
name: wechat-emoji-sticker
description: Create original animated WeChat sticker packs from one or more user-provided images, including 9–12 labeled looping GIF stickers and all companion upload artwork. Use when a user asks for a WeChat emoji/sticker pack, animated stickers, or help preparing/submitting one to the WeChat Sticker Platform.
---

# WeChat Emoji Sticker Pack

Turn one or more user-provided photos into a coherent, submission-ready animated sticker album. Support people, pets, and other subjects the user has authority to use. Work from the images as visual references; do not assume the subject is a dog or reuse details from an unrelated pack.

## Start every new pack by choosing the upload mode

Before generating assets, ask the user to choose:

- **Manual upload**: create the finished files and a clearly organized package for the user to upload.
- **Automatic upload**: create the files and submit them through the WeChat Sticker Platform using an available, approved browser/computer-use integration. Tell the user in the same question that automatic upload will consume additional credits. Their choice of automatic upload authorizes the submission for this task; do not ask them a second time merely to confirm that same upload. If the required browser-control integration is unavailable, finish the package and explain the blocker instead of claiming submission.

Do not start pack generation until the user answers the mode question. If they already specified the mode in the current request, do not ask again.

## Create the pack

1. Use the provided image or images as references for the same requested subject. If the images appear to depict different subjects and the user did not say to combine them, ask whether to make separate albums. Keep likeness/features respectful and consistent.
2. Ask for preferred visual style and wording only if the user has not provided enough direction and the choice materially changes the result. Otherwise choose a clean, expressive style suited to small chat stickers and concise everyday expressions in the user's language.
3. Create **9–12 distinct expressions**. Choose a useful set for the context or let the user specify it. Give every sticker a matching Chinese meaning label when Chinese is requested, and use short, ordered filenames such as `01-开心.gif`. Keep labels in the platform meaning field/manifest unless the user asks for words drawn on the artwork.
4. Keep the character design, proportions, palette, outlines, and rendering consistent across the set. Make the pose and expression distinct in each sticker and readable at chat size. Generate genuine animation with multiple frames and an infinite loop. Do not present a static zoom, pan, or pulse as a designed animated sticker.
5. Create all companion images for the album: a distinct detail-page banner, cover, chat-page icon, appreciation guide image, and appreciation thank-you image. Match the same subject and album concept. Do not put text on image assets unless the relevant platform field explicitly requires it; keep guidance wording in its text field. Avoid adding logos or copyrighted elements without authorization.
6. Organize outputs in one album folder with the 9–12 individual GIFs, a `投稿素材` folder for companion art, and a small manifest listing expression labels, file names, and album metadata. Include a ZIP for manual upload when useful, without unrelated source photos or temporary drafts.

## Validate and review

Use `python scripts/validate_pack.py <pack-folder>` for a structural preflight. The script accepts 9–12 expression labels with `--labels`; without it, it checks the common nine-expression Chinese set. It validates GIF animation/loop structure and known companion-image dimensions. It cannot judge likeness, visual clarity, text, originality, or actual visual compliance; inspect the GIFs and all five companion images before delivery.

Use [references/wechat-upload-checklist.md](references/wechat-upload-checklist.md) for the user's supplied, point-in-time dimensions and visual guidance. Recheck the current platform page before each submission because limits and fields can change. Treat dimensions and byte thresholds separately: some upload fields compress oversized files, while profile fields in the supplied screenshots have hard limits.

## Upload

For manual mode, provide the organized output path and concise field-by-field upload guidance. For automatic mode, fill the album information, upload each GIF and Chinese meaning, set the key-frame thumbnail, attach banner/cover/icon/appreciation guide/thank-you images, then verify the visible upload result. Do not claim success before the page confirms it. If submission errors, inspect the page and retry only after correcting the actual failed field. Do not repeatedly resubmit an album that has already succeeded.
