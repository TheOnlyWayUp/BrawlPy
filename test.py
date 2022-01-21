import brawlpy
import asyncio
import json

client = brawlpy.Client("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImVlMDY3Yjg5LTFhZWQtNDk4Yy1hYmVmLTU1Y2QwNWJhNTc3MSIsImlhdCI6MTY0Mjc1NDYxOCwic3ViIjoiZGV2ZWxvcGVyLzJlNjUxMTJkLWQ0NWUtOTI1OC04NjQ5LTg0ZDA3NDQ3YzA3NSIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiMTcxLjYwLjE1Mi4xNzIiXSwidHlwZSI6ImNsaWVudCJ9XX0.-LLTV-kybO--NHvGcDECrE2Pn6tRVzR8LHzFXkimN63cdgF3MVxMnPrtsElWC2AVuOnii--T0h5ZQf0HFyDptQ")

async def main():
    club = await client.get_club("PVQ0RP90")
    print(club.name)
    print(club.tag)
    for each in club.members:
        print(each)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())