import pytest

pytest.importorskip('playwright')

from panel_material_ui.widgets import AutocompleteInput, Select, RadioBoxGroup, RadioButtonGroup, CheckButtonGroup

from playwright.sync_api import expect
from tests.util import serve_component, wait_until

pytestmark = pytest.mark.ui


@pytest.mark.parametrize('variant', ["filled", "outlined", "standard"])
def test_autocomplete_input_variant(page, variant):
    widget = AutocompleteInput(name='Autocomplete Input test', variant=variant, options=["Option 1", "Option 2", "123"])
    serve_component(page, widget)

    expect(page.locator(".autocomplete-input")).to_have_count(1)
    expect(page.locator(f"div[variant='{variant}']")).to_have_count(1)


@pytest.mark.parametrize('variant', ["filled", "outlined", "standard"])
def test_select_variant(page, variant):
    widget = Select(name='Select test', variant=variant, options=["Option 1", "Option 2", "Option 3"])
    serve_component(page, widget)

    expect(page.locator(".select")).to_have_count(1)
    expect(page.locator(f".MuiSelect-{variant}")).to_have_count(1)


@pytest.mark.parametrize('color', ["primary", "secondary", "error", "info", "success", "warning"])
def test_radio_box_group_color(page, color):
    widget = RadioBoxGroup(name='RadioBoxGroup test', options=["Option 1", "Option 2", "Option 3"], color=color)
    serve_component(page, widget)

    expect(page.locator(".radio-box-group")).to_have_count(1)
    expect(page.locator(f".MuiRadio-color{color.capitalize()}")).to_have_count(len(widget.options))


@pytest.mark.parametrize('orientation', ["horizontal", "vertical"])
def test_radio_box_group_orientation(page, orientation):
    widget = RadioBoxGroup(name='RadioBoxGroup test', options=["Option 1", "Option 2", "Option 3"], orientation=orientation)
    serve_component(page, widget)

    expect(page.locator(".radio-box-group")).to_have_count(1)
    if orientation == "horizontal":
        rbg_orient = page.locator(".MuiRadioGroup-row")
        expect(rbg_orient).to_have_count(1)


@pytest.mark.parametrize('color', ["primary", "secondary", "error", "info", "success", "warning"])
def test_radio_button_group_color(page, color):
    widget = RadioButtonGroup(
        name='RadioButtonGroup test',
        options=["Option 1", "Option 2", "Option 3"],
        color=color
    )
    serve_component(page, widget)

    expect(page.locator(".radio-button-group")).to_have_count(1)
    if color == "error":
        option_color = page.locator(f".Mui-{color}")
    else:
        option_color = page.locator(f".MuiToggleButton-{color}")
    expect(option_color).to_have_count(len(widget.options))


@pytest.mark.parametrize('orientation', ["horizontal", "vertical"])
def test_radio_button_group_orientation(page, orientation):
    widget = RadioButtonGroup(
        name='RadioButtonGroup test',
        options=["Option 1", "Option 2", "Option 3"],
        orientation=orientation
    )
    serve_component(page, widget)

    expect(page.locator(".radio-button-group")).to_have_count(1)
    expect(page.locator(f".MuiToggleButtonGroup-{orientation}")).to_have_count(1)


@pytest.mark.parametrize('size', ["small", "medium", "large"])
def test_radio_button_group_size(page, size):
    widget = RadioButtonGroup(
        name='RadioButtonGroup test',
        options=["Option 1", "Option 2", "Option 3"],
        size=size
    )
    serve_component(page, widget)

    expect(page.locator(".radio-button-group")).to_have_count(1)
    expect(page.locator(f".MuiToggleButton-size{size.capitalize()}")).to_have_count(len(widget.options))


@pytest.mark.parametrize('color', ["primary", "secondary", "error", "info", "success", "warning"])
def test_check_button_group_color(page, color):
    widget = CheckButtonGroup(
        name='CheckButtonGroup test',
        value=[],
        options=["Option 1", "Option 2", "Option 3"],
        color=color
    )
    serve_component(page, widget)

    expect(page.locator(".check-button-group")).to_have_count(1)
    if color == "error":
        option_color = page.locator(f".Mui-{color}")
    else:
        option_color = page.locator(f".MuiToggleButton-{color}")
    expect(option_color).to_have_count(len(widget.options))


@pytest.mark.parametrize('orientation', ["horizontal", "vertical"])
def test_check_button_group_orientation(page, orientation):
    widget = CheckButtonGroup(
        name='CheckButtonGroup test',
        value=[],
        options=["Option 1", "Option 2", "Option 3"],
        orientation=orientation
    )
    serve_component(page, widget)

    expect(page.locator(".check-button-group")).to_have_count(1)
    expect(page.locator(f".MuiToggleButtonGroup-{orientation}")).to_have_count(1)


@pytest.mark.parametrize('size', ["small", "medium", "large"])
def test_check_button_group_size(page, size):
    widget = CheckButtonGroup(
        name='CheckButtonGroup test',
        value=[],
        options=["Option 1", "Option 2", "Option 3"],
        size=size
    )
    serve_component(page, widget)

    expect(page.locator(".check-button-group")).to_have_count(1)
    expect(page.locator(f".MuiToggleButton-size{size.capitalize()}")).to_have_count(len(widget.options))
