"""
Shared response helpers for MCP tools to prevent information leakage.
"""
import os
from typing import Optional


def sanitize_document_name(filename: Optional[str]) -> Optional[str]:
    """
    Return only the filename component for document identifiers to avoid leaking paths.

    This function strips directory paths from user-supplied identifiers,
    preventing the exposure of sensitive filesystem structure information
    in API responses.

    Args:
        filename: Raw user-supplied document identifier

    Returns:
        The basename of the identifier with trailing separators removed,
        or the original value if it was None or empty
    """
    if not filename:
        return filename

    stripped = filename.strip()
    if not stripped:
        return stripped

    stripped = stripped.rstrip("\\/")
    if not stripped:
        return stripped

    basename = os.path.basename(stripped)
    return basename or stripped
