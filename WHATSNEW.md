# What's New in Plume

**v1.5.8 - 2026-05-16**

---

- **Fixed**: Robustified synchronization — account-level subscription sync failures no longer block article updates for existing feeds.

---

**v1.5.7 - 2026-05-16**

---

- **New Feature**: **Auto-fetch Full Articles**. Plume can now automatically download full content from source websites if the RSS feed only provides summaries. Configurable in Settings.
- **New Feature**: **Explore Randomly Mode**. Discover high-quality international news and tech sources (BBC, Telex, El País, Le Monde, etc.) with a single tap.
- **Improved**: **Robust Synchronization**. The sync engine now handles parsing errors gracefully; a single broken feed will no longer stall the entire update process.
- **Improved**: **Ad & Clutter Removal**. Upgraded the extraction engine for cleaner, distraction-free full-text reading.

---


**v1.5.6 - 2026-05-15**

---

- **Improved**: Relocated podcast mini-player close button to the top-right corner to prevent overlap with long episode titles.
- **Improved**: Robustified version update check to correctly handle and ignore flavor suffixes (e.g., `-std`, `-auto`) during comparison.
- **Fixed**: Resolved compilation errors in Settings where suspend functions were called outside of coroutines.
-  * New Explore Randomly Mode: Discover new high-quality sources from around the world (BBC, Telex, El País, Le Monde, and
     more) with a single tap. Perfect for language practice and breaking out of your filter bubble!
   * Discovery Language Settings: Customize your exploration by selecting your preferred languages (English, Hungarian,
     Spanish, French, German) in Settings.
   * Dual Shuffle Feature:
       * Global Shuffle: Get a random article from all your subscriptions.
       * Contextual Shuffle: Feeling focused? Get a random article from a specific feed or category.
   * OPML Support for Desktop: Windows users can now easily import and export their feed collections.
   * Improved Android Widget: Fixed data loading issues and optimized refresh logic for a more reliable home screen
     experience.
   * Performance & Stability: Fixed several navigation bugs and improved article rendering speed.


---

**v1.5.5 - 2026-05-13**

---

- **Improved**: Podcast mini-player now features a dedicated 'X' close icon for easier dismissal.
- **Fixed**: OPML Export now correctly exports subscriptions from the active service (Feedly, The Old Reader, or Local), fixing the issue where exports appeared empty.

---


**v1.5.4 - 2026-05-12**

---

- **Improved**: Discover dialog reordered — RSS feeds now appear first by default.
- **Fixed**: Release script now correctly builds and packages the latest flavor-specific APK.

---

**v1.5.3 - 2026-05-12**

---

- **Fixed**: Old version published with new version number

---

**v1.5.2 - 2026-05-12**

---

- **Fixed**: DB migration clear all the data

---


**v1.5.1 - 2026-05-12**

---

- **Fixed**: Podcast mini-player controls (play/pause, ±15/30s skip, stop, seek bar) moved from the article reader into `MainActivity` so the player stays visible while navigating — it no longer disappears when the user goes back.
- **Fixed**: "Show all feeds" toggle now persists across app restarts — the setting was being reset to its default every time the app relaunched.
- **Fixed**: CDATA markers (`<![CDATA[...]]>`) no longer appear in article or feed titles fetched from Feedly, TheOldReader, or local RSS feeds.
- **Improved**: RSS/Podcast Discover — country selector now includes 22 languages (up from 7; added IT, PL, NL, PT, RO, CZ, SK, SE, DK, FI, NO, RU, UA, CN, BR). Category searches are now biased toward the selected language by appending a language keyword to the Feedly query. Changing the country while a custom search is active keeps the typed query; switching while the category view is shown reloads with localised terms.
- **Improved**: Floating read all button

---

**v1.5.0 - 2026-05-10**

---

- **Fixed**: Version update check now correctly detects newer versions — previously "1.4.9" was considered newer than "1.4.10" due to string comparison. All users on older versions will now be correctly notified of this and future updates.

---

**v1.4.12 - 2026-05-10**

---

- **Improved**: Battery usage reduced — podcast player polls position less frequently when paused, and the Discover dialog reuses a single HTTP connection pool instead of creating new ones per request.

---


**v1.4.11 - 2026-05-10**

---

- **New Feature**: **YouTube Channel Discovery**. A new "▶ YouTube" tab in Discover shows popular channels by category (🇭🇺 Magyar, News, Tech, Gaming, Finance, and more), updated daily via GitHub Actions. Subscribe with a single tap.
- **Fixed**: HTTP feeds (non-HTTPS) can now be added — the app was silently blocking them on Android 9+.
- **Fixed**: Adding a feed now shows a proper error message if the URL is unreachable or the format is unsupported. Previously it failed silently.
- **Fixed**: Version update check now correctly detects newer versions with double-digit patch numbers (e.g. 1.4.10 > 1.4.9).

---

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
