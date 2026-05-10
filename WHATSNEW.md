# What's New in Plume

**v1.4.10 - 2026-05-10**

---

- **Fixed**: Sync no longer spins forever on feeds with many episodes (e.g. 1000+ entries). The automatic full-text fetch during sync has been removed — it was triggering hundreds of HTTP requests per feed.
- **Fixed**: Articles no longer disappear and reappear during pull-to-refresh. Read article visibility is now only reset after a successful sync, not at the start.
- **Fixed**: RSS parser now caps at 100 articles per feed to avoid processing unnecessarily large feeds.
- **Fixed**: HTTP requests now have a 15s connect / 30s read timeout, preventing the sync from hanging indefinitely on slow servers.

---

**v1.4.9 - 2026-05-10**

---

- **Improved**: **RSS Feed Discovery**. The RSS feeds tab in Discover now includes a search powered by the Feedly API — find popular feeds worldwide by keyword, filtered by country/language. The curated list remains as the default view.

---

**v1.4.8 - 2026-05-10**

---

- **Fixed**: CDATA markers (`<![CDATA[...]]>`) no longer appear as visible text at the top of articles. The fix handles all casing variants and works for titles, descriptions, and encoded content fields.

---

**v1.4.7 - 2026-05-10**

---

- **New Feature**: **Built-in Podcast Player**. Podcast episodes now play directly in the app — no external app needed. Includes play/pause, seek bar, –15s / +30s skip, and background playback with lock screen controls.
- **New Feature**: **Podcast Discovery**. Tap "+" → "Discover / Popular" to browse top podcasts by country (🇭🇺 HU, 🇺🇸 US, 🇬🇧 GB, and more) and category (News, Tech, Comedy, Science, Sports, and more) powered by the iTunes Charts. Search by keyword or browse by genre — subscribe with a single tap.
- **New Feature**: **YouTube Link Handling**. Articles containing YouTube links now show a "Watch on YouTube" button. Preferred app (NewPipe, YouTube, or always ask) is configurable in Settings → Media.

---

**v1.4.5 - 2026-05-10**

---

- **New Feature**: **Built-in Podcast Player**. Podcast episodes now play directly in the app — no external app needed. Includes play/pause, seek bar, –15s / +30s skip, and background playback with lock screen controls.
- **New Feature**: **Podcast Discovery**. Tap "+" → "Discover / Popular" to browse the top podcasts by country (🇭🇺 HU, 🇺🇸 US, 🇬🇧 GB, and more) powered by the iTunes Charts. Search by keyword and subscribe with a single tap.
- **New Feature**: **YouTube Link Handling**. Articles containing YouTube links now show a "Watch on YouTube" button. Preferred app (NewPipe, YouTube, or always ask) is configurable in Settings → Media.

---

**v1.4.4 - 2026-05-10**

---

- **New Feature**: **YouTube Channel Support**. Add any YouTube channel by pasting its URL (e.g. `youtube.com/@channelname`). Plume automatically resolves it to the channel's RSS feed — no API key needed.
- **New Feature**: **Popular Feeds Browser**. Tap "Popular feeds" in the Add Feed dialog to browse a curated list of popular sources (BBC, Hacker News, The Verge, Reddit, NASA, and more) and add any with a single tap.
- **Fixed**: The URL input field in the Add Feed dialog no longer allows multi-line text entry.

---

**v1.4.3 - 2026-05-08**

---

- **Fix** Sync failed when pull down

---

**v1.4.0 - 2026-05-08**

---

- **New Feature**: **Global Search**. Search through all cached articles by keyword across all feeds.
- **New Feature**: **Search FAB**. Quickly access search from the home screen via a dedicated floating button.
- **New Feature**: **Dynamic FAB Placement**. Buttons move to the left side when 'Left-handed mode' is enabled for better ergonomics.

---

**v1.3.3 - 2026-05-08**

---

- **Fix** Version check

---

**v1.3.2 - 2026-05-08**

---

- **New Feature**: **Customizable Gestures**. Choose between 'Mark as read', 'Star', or 'Share' for swipe actions.
- **New Feature**: **Left-handed Mode**. Toggle swipe directions in Settings for better accessibility.
- **New Feature**: **Linger to Read**. Automatically mark articles as read by simply staying on them in the list (optional).
- **Improved**: **Scroll Retention**. Returning from an article now preserves your exact scroll position in the list.

---


**v1.3.1 - 2026-05-08**

---

- **New Feature**: **Check for updates**. Manually check GitHub for the latest Plume release directly from Settings.

---


**v1.3.0 - 2026-05-08**

---

- **New Feature**: **Local Mode (No Account)**. Use the app completely anonymously without signing up for any service.
- **New Feature**: **Import/Export (OPML)**. Easily migrate your subscriptions to and from other RSS readers.
- **New Feature**: **Toolbar Navigation**. All main actions (Sync, Saved, Settings) moved to the top bar for better stability.
- **New Feature**: **Rename Feeds**. Long-press any feed in the list to give it a custom name.
- **New Feature**: **Compact & Optimize**. New database maintenance tool to cleanup old data and defragment storage.
- **New Feature**: **Unsubscribe Gesture**. Swipe left on any feed to quickly remove it.
- **Improved**: **Smart Sync**. Local read, starred, and saved states are now preserved and never overwritten by server updates.
- **Improved**: **History Retention**. Read articles are no longer automatically deleted, allowing you to browse your reading history.
- **Improved**: **UI Persistence**. The "Show read articles" toggle state is now saved across app restarts.
- **Improved**: **List Navigation**. Automatically scroll to the top when toggling the read articles filter.
- **Improved**: **RSS Engine**. Better support for CDATA sections, Atom feeds, and various XML title formats.
- **Improved**: **Background Sync**. Smarter logic to only sync services you are actually logged into.
- **Improved**: **Release Automation**. Fully automated script to find, copy, and publish APKs to GitHub.
- **Fixed**: Resolved issues with the Toolbar back button not responding on certain devices.
- **Fixed**: Fixed 401 errors in background sync when using Local mode.

---

**v1.1.0 - 2026-05-08**

---

- **New Feature**: **Local Mode (No Account)**. Use the app anonymously and add your own RSS/Atom feeds directly.
- **New Feature**: **Import/Export (OPML)**. Easily move your feed list between apps.
- **New Feature**: **Unsubscribe** from feeds using a left swipe on the main list or via the menu inside a feed.
- **New Feature**: Added swipe gestures for easier navigation. Swipe right on a feed to open its articles, and swipe left on the article list to go back.
- **Improved**: Unread article counts in the feed list now update instantly in real-time when articles are read.
- **Fixed**: Enhanced RSS Parser to better handle CDATA sections and various title formats.
- **Fixed**: Internal database optimizations and build stability fixes.

**v1.0.0 - 2026-05-06**

---

- Initial release of Plume RSS Reader.
- Support for Feedly and TheOldReader.
- Offline mode and image caching.
- Text-to-Speech integration.
- Home screen widget.
- Dark mode support.
