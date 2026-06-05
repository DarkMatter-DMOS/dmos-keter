import pytest
from keter import CausalEngine

@pytest.mark.asyncio
async def test_parse_goal():
    engine = CausalEngine()
    goal = engine.parse_goal("reduce latency")
    assert goal["text"] == "reduce latency"

@pytest.mark.asyncio
async def test_decompose():
    engine = CausalEngine()
    goal = {"text": "test", "type": "atomic"}
    subgoals = engine.decompose(goal)
    assert len(subgoals) == 1
    assert subgoals[0]["text"] == "test"

@pytest.mark.asyncio
async def test_reason_without_fabric():
    engine = CausalEngine()
    with pytest.raises(RuntimeError, match="No fabric attached"):
        await engine.execute(goal={"text": "test"})
