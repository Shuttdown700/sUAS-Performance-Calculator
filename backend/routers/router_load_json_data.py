from fastapi import APIRouter
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from backend.utils.load_json_data import load_json_data

router = APIRouter(prefix="/components", tags=["components"])

@router.get("/")
def get_components():
    """API endpoint to retrieve all drone components."""
    return load_json_data()

@router.get("/{category}")
def get_component_category(category: str):
    """API endpoint to retrieve a specific component category."""
    components = load_json_data()
    return components.get(category, [])