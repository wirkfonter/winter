import dataclasses
import pytest

from winter.web import ResponseEntity


@dataclasses.dataclass
class Dataclass:
    pass


def test_response_entity_fails_without_nested_type():
    with pytest.raises(TypeError, match=r"Using TypeWrapper without nested type is forbidden, use TypeWrapper\[T\]"):
        ResponseEntity("foo")


def test_response_entity_fails_with_wrong_nested_type():
    with pytest.raises(TypeError, match="Types mismatch: <class 'str'> and <class 'test_response_entity.Dataclass'>"):
        ResponseEntity[Dataclass]("foo")


def test_response_entity_has_nested_type():
    assert ResponseEntity[Dataclass]._nested_type is Dataclass
    assert ResponseEntity[Dataclass](Dataclass())._nested_type is Dataclass
