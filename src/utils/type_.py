import pyarrow as pa


def type_convert(py_):
    _ = None
    schemas_ = []
    for v in py_:
        if isinstance(v, str):
            _ = (v, pa.string())
        elif isinstance(v, int):
            _ = (v, pa.int64())
        elif isinstance(v, float):
            _ = (v, pa.float64())
        elif isinstance(v, list):
            ty = pa.map_(pa.string(), pa.int64(), pa.float64())
            _ = (v, pa.array(v, type=ty))
        else:
            _ = (v, pa.string())
        schemas_.append(_)
    return pa.schema(schemas_)
