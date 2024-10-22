import sys
import networkx as nx
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QMessageBox
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from src.parse_input import parse_input

class GraphApp(QMainWindow): 
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simulation Data Generator")
        self.setGeometry(100, 100, 800, 600)

        # Main widget and layout
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        self.layout = QVBoxLayout(main_widget) # type: ignore

        # Text box for input
        self.input_box = QTextEdit(self)
        self.input_box.setPlaceholderText("Example:\nnode: A ~ Bern(0.5)\nnode: B\nedge: A B\n")
        self.layout.addWidget(self.input_box)

        # Button to generate data
        self.generate_button = QPushButton("Generate Data", self)
        self.generate_button.clicked.connect(self.generate_data)
        self.layout.addWidget(self.generate_button)

        # Matplotlib canvas for drawing graph
        self.canvas = FigureCanvas(plt.Figure()) # type: ignore
        self.layout.addWidget(self.canvas)
        self.ax = self.canvas.figure.subplots()

        # Graph structure (NetworkX)
        self.graph = nx.DiGraph()

    # Parse the input from the text box and create nodes and edges
    def parse_input(self):
        

    # Draw the graph using matplotlib
    def draw_graph(self):
        self.ax.clear()  # Clear previous graph
        pos = nx.spring_layout(self.graph)

        # Draw nodes and edges
        nx.draw(self.graph, pos, ax=self.ax, with_labels=True, node_color="skyblue", node_size=3000, edge_color="gray", font_size=12, font_color="black")
        self.canvas.draw()

    # Generate and display simulated data
    def generate_data(self):

        self.graph, error_msg, funcs = parse_input(text=self.input_box.toPlainText())
        self.parse_input()
        self.draw_graph()

        # Example: Generate simple data (number of neighbors per node)
        simulated_data = {node: len(list(self.graph.neighbors(node))) for node in self.graph.nodes()}
        QMessageBox.information(self, "Simulated Data", f"Node connections:\n{simulated_data}")
