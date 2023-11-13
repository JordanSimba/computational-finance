"""
Get data for a particular set of option contracts and their tickers
https://www.okx.com/docs-v5/en/#public-data-rest-api-get-option-market-data
"""
import time
import logging
import aiohttp
import asyncio

from datetime import datetime, timedelta

from data_models import (
    InstrumentRequest,
    InstrumentResponse,
    OptionSummaryRequest,
    OptionSummaryResponse
)

OKX_BASE_URL = "https://www.okx.com"

logging.basicConfig(level='INFO')
logger = logging.getLogger(__name__)


async def get_option_market_data(base_url: str, request: OptionSummaryRequest) -> OptionSummaryResponse:
    # EP GET /api/v5/public/opt-summary
    end_point = "api/v5/public/opt-summary"
    response = await http_get(f"{base_url}/{end_point}", params=no_nulls(request.to_dict()))
    return OptionSummaryResponse.from_dict(response)
    

async def get_instrument_data(base_url: str, request: InstrumentRequest) -> InstrumentResponse:
    end_point = "api/v5/public/instruments"
    response = await http_get(f"{base_url}/{end_point}", params=no_nulls(request.to_dict()))
    return InstrumentResponse.from_dict(response)


async def http_get(url,  params=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            logger.info(f"Making request to {url=}, {params=}")
            return await response.json()


def no_nulls(_dict):
    return {k: v for k, v in _dict.items() if v is not None}


def get_epoch_start():
    # https://docs.python.org/3/library/time.html#time.struct_time
    time_struct = time.gmtime(0)
    return datetime(year=time_struct.tm_year, month=time_struct.tm_mon, day=time_struct.tm_mday)


def millisecond_to_datetime(ms):
    return get_epoch_start() + timedelta(milliseconds=ms)


if __name__ == "__main__":
    opt_summary_req = OptionSummaryRequest(underlying='BTC-USD')
    res = asyncio.run(get_option_market_data(OKX_BASE_URL, opt_summary_req))
    print(len(res.data))
    print(res.data[:1])

    first_op = res.data[0]
    first_opt_inst_id = first_op.instId
    first_opt_uly = first_op.uly
    first_opt_type = first_op.instType
    instrument_req =  InstrumentRequest(
        instrument_id=first_opt_inst_id,
        instrument_type=first_opt_type,
        underlying=first_opt_uly
    )
    instrument_req =  InstrumentRequest(
        instrument_id='BTC-USD-240628-32000-C',
        instrument_type='OPTION',
        underlying='BTC-USD'
    )
    res = asyncio.run(get_instrument_data(OKX_BASE_URL, instrument_req))
    print(len(res.data))
    print(res.data[:1])
    