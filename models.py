from dataclasses import dataclass, field


@dataclass
class ScoreItem:
    """
    Representerar en enskild poängpost i en strategi.
    """

    name: str
    points: float
    max_points: float
    comment: str


@dataclass
class Metrics:
    """
    Samlar alla nyckeltal som används i TradingLab.
    Alla fält är frivilliga eftersom olika strategier använder olika mått.
    """

    #
    # QUALITY
    #

    operating_margin: float | None = None
    debt_ratio: float | None = None
    roe: float | None = None
    revenue_growth: float | None = None
    profit_growth: float | None = None

    #
    # VALUE
    #

    pe: float | None = None
    ps: float | None = None
    pb: float | None = None
    dividend_yield: float | None = None
    ev_ebit: float | None = None
    ev_ebitda: float | None = None
    roic: float | None = None
    peg: float | None = None


@dataclass
class AnalysisResult:
    """
    Resultatet från en strategi.
    """

    score: float
    metrics: Metrics
    comments: list[str] = field(default_factory=list)

    #
    # Transparens i poängsättningen
    #

    score_items: list[ScoreItem] = field(default_factory=list)