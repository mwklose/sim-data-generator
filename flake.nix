{
  description = "Python app with Qt GUI";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";  # Using nixos-unstable for up-to-date packages
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }: flake-utils.lib.eachDefaultSystem (system: let
    pkgs = import nixpkgs { inherit system; };

    # Python environment with PyQt5 (Qt for Python)
    pythonEnv = pkgs.python312.withPackages (ps: with ps; [
      pyqt5       # PyQt5 for Qt support
      polars      # polars
      numpy
      statsmodels 
      networkx
      matplotlib
    ]);

  in {
    # Defining the default package, built using the Python environment
    packages.default = pkgs.mkShell {
      buildInputs = [ 
        pythonEnv 
        pkgs.qt5.full
      ];  # Adding the Python environment to the build inputs
    };

    # DevShell allows interactive development
    devShells.default = pkgs.mkShell {
      buildInputs = [ 
        pythonEnv 
        pkgs.qt5.full
      ];
    };

    # A NixOS module for adding the app to a NixOS configuration
    nixosModules.default = {
      config, pkgs, ... }: {
        environment.systemPackages = [ 
          pythonEnv 
          pkgs.qt5.full
        ];
      };
  });
}