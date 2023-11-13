from dataclasses_json import Undefined, config, dataclass_json
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclass
class InstrumentData:
    # https://www.okx.com/docs-v5/en/?shell#public-data-rest-api-get-instruments
    # below is a truncated set of properties compared to the full api response
    # application doesn't need all of them so simply dropping the unnecessary
    instType: str
    instId: str
    instFamily: str
    uly: str
    category: str
    baseCcy: str
    quoteCcy: str
    settleCcy: str
    ctVal: str
    ctMult: str
    ctValCcy: str
    optType: str
    stk: str
    listTime: str
    expTime: str
    state: str


@dataclass_json
@dataclass
class InstrumentResponse:
    code: str
    msg: str
    data: List[InstrumentData]


@dataclass_json
@dataclass
class OptionMarketData:
    instType: str
    instId: str
    uly: str
    delta: str
    gamma: str
    theta: str
    vega: str
    deltaBS: str
    gammaBS: str
    thetaBS: str
    vegaBS: str
    realVol: str
    volLv: str
    bidVol: str
    askVol: str
    markVol: str
    lever: str
    fwdPx: str
    ts: str


@dataclass_json
@dataclass
class OptionSummaryResponse:
    code: str
    msg: str
    data: List[OptionMarketData]


@dataclass_json
@dataclass
class InstrumentRequest:
    instrument_type: str = field(metadata=config(field_name="instType"))
    # Either underlying or instrument_family is required. If both are passed, instrument_family will be used.
    underlying: Optional[str] = field(default=None, metadata=config(field_name="uly"))
    instrument_family: Optional[str] = field(default=None, metadata=config(field_name="instFamily"))
    instrument_id: Optional[str] = field(default=None, metadata=config(field_name="instId"))


@dataclass_json
@dataclass
class OptionSummaryRequest:
    # Either underlying or instrument_family is required. If both are passed, instrument_family will be used.
    underlying: Optional[str] = field(default=None, metadata=config(field_name="uly"))
    instrument_family: Optional[str] = field(default=None, metadata=config(field_name="instFamily"))
    # Contract expiry date, the format is "YYMMDD", e.g. "200527"
    expiration: Optional[str] = field(default=None, metadata=config(field_name="expTime"))