from pathlib import Path

import pytest

from changelog_manager.utils import ChangelogManager


def test_changelog_init(tmp_path):
    tmp_changelog_path = tmp_path / "changelog_init.md"
    tmp_changelog = str(tmp_changelog_path)

    assert not tmp_changelog_path.exists()

    ChangelogManager.init(tmp_changelog)
    assert tmp_changelog_path.exists()
    assert tmp_changelog_path.is_file()

    with pytest.raises(FileExistsError):
        ChangelogManager.init(tmp_changelog)

    ChangelogManager.init(tmp_changelog, force=True)
    assert tmp_changelog_path.exists()
    assert tmp_changelog_path.is_file()

    cm = ChangelogManager(tmp_changelog)
    assert cm.current is None
    assert cm.suggest is None
    assert cm.display("unreleased") == "## [unreleased] - None\n"
