from unittest.mock import create_autospec, ANY

import pytest
import app
import pandas as pd


def test_update_graph(monkeypatch):
    mock_df = pd.DataFrame({
        "country": ["canada", "brasil"],
        "year": [1995, 1995],
        "pop": [1, 2]
    })
    monkeypatch.setattr(app, "df", mock_df)

    mock_px = create_autospec(app.px)
    monkeypatch.setattr(app, "px", mock_px)

    assert app.update_graph("canada") == mock_px.line.return_value

    mock_px.line.assert_called_once_with(ANY, x="year", y="pop")
