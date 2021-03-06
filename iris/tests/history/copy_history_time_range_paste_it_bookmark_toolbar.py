# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.


from iris.test_case import *


class Test(BaseTest):

    def __init__(self):
        BaseTest.__init__(self)
        self.meta = 'Copy a history time range from the Library and paste it into the Bookmark Toolbar.'
        self.test_case_id = '174034'
        self.test_suite_id = '2000'
        self.locales = ['en-US']

    def run(self):
        show_all_history_pattern = LibraryMenu.HistoryOption.SHOW_ALL_HISTORY
        iris_bookmark_pattern = Pattern('iris_bookmark.png')
        iris_bookmark_focus_pattern = Pattern('iris_bookmark_focus.png')
        bookmarks_toolbar_most_visited_pattern = SidebarBookmarks.BookmarksToolbar.MOST_VISITED
        view_bookmarks_toolbar = LibraryMenu.BookmarksOption.BookmarkingTools.VIEW_BOOKMARKS_TOOLBAR
        today_bookmarks_toolbar_pattern = Pattern('today_bookmarks_toolbar.png')
        history_today_pattern = Pattern('history_today.png')

        # Open the Bookmarks toolbar.
        access_bookmarking_tools(view_bookmarks_toolbar)
        expected = exists(bookmarks_toolbar_most_visited_pattern, 10)
        assert_true(self, expected, 'Bookmarks Toolbar has been activated.')

        # Open History and check if it is populated with the Iris page.
        open_library_menu('History')

        right_upper_corner = Region(SCREEN_WIDTH / 2, 0, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        expected = right_upper_corner.exists(iris_bookmark_pattern, 10)
        assert_true(self, expected, 'Iris page is displayed in the History menu list.')

        click(show_all_history_pattern)

        expected = exists(iris_bookmark_focus_pattern, 10)
        assert_true(self, expected, 'Iris page is displayed in the Recent History list.')

        # Copy the History time range from the Library and paste it to the Bookmarks toolbar.
        right_click(history_today_pattern)
        type(text='c')

        click_auxiliary_window_control('close')
        time.sleep(DEFAULT_UI_DELAY)

        right_click(bookmarks_toolbar_most_visited_pattern)
        type(text='p')

        expected = exists(today_bookmarks_toolbar_pattern)
        assert_true(self, expected, 'History time range was copied successfully to the Bookmarks toolbar.')
