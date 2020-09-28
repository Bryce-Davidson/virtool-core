from dataclasses import dataclass
from typing import Optional, MutableMapping, Awaitable, Callable, Iterable
import virtool_core.caches.db

Processor = Callable[["DB", MutableMapping], Awaitable[MutableMapping]]
DatabaseUpdateListener = Callable[[str, str, Iterable[str]], Awaitable[None]]


@dataclass
class CollectionBinding:
    collection_name: str
    projection: Optional[MutableMapping] = None
    processor: Optional[Callable[["DB", MutableMapping], Awaitable[MutableMapping]]] = None
    silent: bool = False


# TODO: set projections for modules
BINDINGS = [
    CollectionBinding("analyses"),
    CollectionBinding("caches", projection=virtool_core.caches.db.PROJECTION),
    CollectionBinding("coverage"),
    CollectionBinding("files"),
    CollectionBinding("groups"),
    CollectionBinding("history"),
    CollectionBinding("hmm"),
    CollectionBinding("indexes"),
    CollectionBinding("jobs"),
    CollectionBinding("keys"),
    CollectionBinding("kinds"),
    CollectionBinding("otus"),
    CollectionBinding("processes"),
    CollectionBinding("references"),
    CollectionBinding("samples"),
    CollectionBinding("settings"),
    CollectionBinding("sequences"),
    CollectionBinding("sessions"),
    CollectionBinding("status"),
    CollectionBinding("subtraction"),
    CollectionBinding("users"),
]
