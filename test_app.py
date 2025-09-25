import dash
from dash import html, dcc
import pytest
from app import app as dash_app

def test_present_header(dash_duo):
    dash_duo.start_server(dash_app)
    header_element = dash_duo.wait_for_element('h1', timeout=10)
    assert header_element.text == 'Pink Morsel Sales'

def test_visualisation(dash_duo):
    dash_duo.start_server(dash_app)
    graph_element = dash_duo.wait_for_element('#graph-output', timeout=10)
    assert graph_element is not None

def test_region_picker(dash_duo):
    dash_duo.start_server(dash_app)
    radio_items_element = dash_duo.wait_for_element('#radio-items-input', timeout=10)
    assert radio_items_element is not None