"""
サンプルモジュール。
"""

from dataclasses import dataclass


def add(a: int, b: int) -> int:
    """
    2つの整数を加算する。

    Args:
        a: 1つ目の整数。
        b: 2つ目の整数。

    Returns:
        a + b の結果。
    """
    return a + b


@dataclass
class Greeter:
    """
    挨拶を生成するクラス。

    Attributes:
        name: 名前。
    """

    name: str

    def greet(self) -> str:
        """
        挨拶文を返す。

        Returns:
            挨拶メッセージ。
        """
        return f"Hello, {self.name}"