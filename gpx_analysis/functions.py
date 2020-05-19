import gpxpy
from pathlib import Path
import pandas as pd

def test(gpx_file_name : str):
    root = Path(__file__).parent
    file_name = root / "data" / gpx_file_name

    gpx_file = open(file_name, 'r')

    gpx = gpxpy.parse(gpx_file)

    print(f"GPX file '{gpx_file_name}' has {len(gpx.tracks)} track(s):")

    for t, track in enumerate(gpx.tracks):
        print(f"\t- Track {t}:'{track.name}' has {len(track.segments)} segment(s)")
        for i,segment in enumerate(track.segments):
            print(f"\t\t- Segment {i} has {len(segment.points)} points")

def test1(gpx_file_name : str):
    root = Path(__file__).parent
    file_name = root / "data" / gpx_file_name

    gpx_file = open(file_name, 'r')

    gpx = gpxpy.parse(gpx_file)

    df = pd.DataFrame()

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                for ext in point.extensions:
                    print(ext.tag)
                    point_extensions = {}
                    for extchild in list(ext):
                        tag_name = extchild.tag.split("}")[1]
                        print('{0} -> {1}'.format(tag_name, extchild.text))
                        point_extensions[tag_name] = extchild.text

                    df2 = pd.DataFrame([list(point_extensions.values())], columns=list(point_extensions.keys()))
                    df = df.append(df2, ignore_index=True)

    print(df)





def test2(gpx_file_name : str):
    root = Path(__file__).parent
    file_name = root / "data" / gpx_file_name

    gpx_file = open(file_name, 'r')

    gpx = gpxpy.parse(gpx_file)

    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))

    for waypoint in gpx.waypoints:
        print('waypoint {0} -> ({1},{2})'.format(waypoint.name, waypoint.latitude, waypoint.longitude))

    for route in gpx.routes:
        print('Route:')
        for point in route.points:
            print('Point at ({0},{1}) -> {2}'.format(point.latitude, point.longitude, point.elevation))



