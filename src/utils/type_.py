import pyarrow as pa


def type_convert(pydict: dict):
    _ = None
    schemas_ = []
    for k, v in pydict.items():
        if isinstance(v, str):
            _ = (k, pa.string())
        elif isinstance(v, int):
            _ = (k, pa.int64())
        elif isinstance(v, float):
            _ = (k, pa.float64())
        elif isinstance(v, list):
            ty = pa.map_(pa.string(), pa.int64(), pa.float64())
            _ = (k, pa.array(v, type=ty))
        else:
            _ = (k, pa.string())
        schemas_.append(_)
    return pa.schema(schemas_)
