from typing import Any, Dict, Tuple
import networkx as nx


def parse_input(text: str) -> Tuple[nx.DiGraph, str | None, Dict[str, Any]]:
    """Dedicated function for parsing the text box input.

    Args:
        text (str): The raw text from the application.

    Returns:
        Tuple[nx.DiGraph, str, Dict[str, Any]]: 
            a Directed Graph with edges, 
            a string containing a possible error message (or None, if no error), 
            and a dictionary used in the data generation step.
    """

    graph = nx.DiGraph()
    input_text = text.strip().split("\n")

    for line in input_text:
        line = line.strip().lower()
        # Match based on starting value
        if line.startswith("node:"):
            # Valid node syntax: 
            # single-node: Y
            # single-sim node: Y ~ Bern(0.5)
            # multi-sim node: Y ~ Bern(0.1 + 0.5 * A)
            # zero-sim node: Y ~ 1
            node_name = line.split(sep="node:")[1].strip()
            graph.add_node(node_name)
        elif line.startswith("edge:"):
            # Valid edge syntax: 
            # single-edge: Y Z 
            # multi-edge: Y -> Y1 Y2 Y3
            nodes = line.split("edge:")[1].strip().split()
            if len(nodes) == 2:
                graph.add_edge(nodes[0], nodes[1])

        elif line.startswith("intervene:"): 
            # Valid intervention syntax: 
            # Allowed to have multiple interventions; creates "potential outcomes" column for downstream.
            # intervene: A = 1
            # intervene: A = 0
            # intervene: A = (L < 200)
            
            ...
        
    raise Exception("[ParseInput] Not implemented.")

def _parse_equation(eqn: str) -> Tuple[str, str]:
    """Parses an equation of the form 'Y ~ Bern(0.1 + 0.3 * A)'

    Args:
        eqn (str): _description_

    Returns:
        Tuple[str, str]: _description_
    """
    ...