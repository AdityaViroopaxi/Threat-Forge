def ioc_schema(ioc, ioc_type, sources, score, category, last_seen, details):
    return {
        "ioc": ioc,
        "type": ioc_type,
        "sources": sources,
        "score": score,
        "category": category,
        "last_seen": last_seen,
        "details": details
    }
