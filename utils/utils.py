import os
import webbrowser


def render_and_open(chart, filename: str = "chart.html"):
    """
    Renders a Pyecharts chart to ./output/filename and opens it in the default browser.

    Args:
        chart (Chart): A Pyecharts chart instance.
        filename (str): Output HTML filename (default: "chart.html").
    """
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)  # Ensure output directory exists
    output_path = os.path.join(output_dir, filename)
    
    chart.render(output_path)
    file_path = os.path.abspath(output_path)
    webbrowser.open(f"file://{file_path}")
