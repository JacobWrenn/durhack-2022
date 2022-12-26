{
  description = "flask-app";
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };
  outputs = { self, nixpkgs, flake-utils, ... }:
    with flake-utils.lib;
    eachSystem allSystems (system:
      let
        myNixPkgs = nixpkgs.legacyPackages.${system};

        pythonApp = myNixPkgs.stdenvNoCC.mkDerivation rec {
          name = "flask-app";
          src = self;
          nativeBuildInputs = [
            myNixPkgs.python310
            myNixPkgs.python310Packages.flask
            myNixPkgs.python310Packages.gunicorn
            myNixPkgs.python310Packages.requests
          ];

          installPhase = ''
            mkdir -p $out
            cp -r server/* $out/
            echo "#!/bin/sh
            ${myNixPkgs.python310Packages.gunicorn}/bin/gunicorn --bind 0.0.0.0:5000 wsgi:app" > $out/bootstrap.sh
          '';
        };

        myDevTools = with myNixPkgs; [
          nodejs-18_x
          nodePackages.vue-cli
          nodePackages.serve
          yarn
          postman

          pandoc

          python310
          python310Packages.flask
          python310Packages.pip
          python310Packages.gunicorn
          python310Packages.requests
          python310Packages.flask-cors
          python310Packages.matplotlib
          python310Packages.numpy
        ];
      in
      rec {
        packages = {
          pythonPkg = pythonApp;
          default = packages.pythonPkg;
        };

        apps.default = {
          type = "app";
          program = "${packages.pythonPkg}/bootstrap.sh";
        };
        
        devShell = myNixPkgs.mkShell {
          nativeBuildInputs = myDevTools;
        };
      });
}

