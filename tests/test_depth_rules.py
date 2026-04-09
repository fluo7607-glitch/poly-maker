import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from trading import _queue_ahead_size, _is_thin_depth


def test_queue_ahead_size_for_buy_uses_better_bids_only():
    bids = {
        0.82: 30.0,
        0.81: 40.0,
        0.80: 100.0,
    }
    assert _queue_ahead_size(bids, "buy", 0.81) == 30.0


def test_queue_ahead_size_for_sell_uses_better_asks_only():
    asks = {
        0.18: 50.0,
        0.19: 60.0,
        0.20: 70.0,
    }
    assert _queue_ahead_size(asks, "sell", 0.19) == 50.0


def test_thin_depth_threshold_is_less_or_equal_two_x_min_size():
    assert _is_thin_depth(100.0, 50.0) is True
    assert _is_thin_depth(99.99, 50.0) is True
    assert _is_thin_depth(100.01, 50.0) is False
