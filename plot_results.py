# plot_results.py

import click
import pandas as pd
import plotly.express as px
from pathlib import Path

DEFAULT_METRICS = ["Cosine Sim", "BLEU", "ROUGE-1", "ROUGE-L"]

@click.command()
@click.option("--csv-path", default="results/summarization-comparison/results.csv", help="Path to CSV file")
@click.option("--metric", type=click.Choice(DEFAULT_METRICS), help="Metric to plot")
@click.option("--show", is_flag=True, help="Show plot in browser")
@click.option("--save", is_flag=True, help="Save plot as PNG")
def main(csv_path, metric, show, save):
    df = pd.read_csv(csv_path)
    output_dir = Path(csv_path).parent

    if metric:
        metrics = [metric]
    else:
        metrics = DEFAULT_METRICS

    for m in metrics:
        fig = px.bar(
            df,
            x="Model",
            y=m,
            color="Prompt",
            barmode="group",
            title=f"{m} by Model and Prompt",
            template="plotly_white",
            height=500,
            hover_data={
                "Prompt": True,
                "Latency": True,
                "Num Tokens": True,
                "Output": True,
                m: True,
                "Model": False,  # already shown
            }
        )


        if save:
            filename = output_dir / f"{m.lower().replace(' ', '_')}.png"
            fig.write_image(str(filename))
            print(f"✅ Saved: {filename}")

        if show:
            fig.show()

if __name__ == "__main__":
    main()
