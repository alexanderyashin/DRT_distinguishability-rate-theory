# ============================================
# Makefile — DRT Platinum
# ============================================

PYTHON ?= python3
PIP ?= pip3

ROOT_DIR := $(shell pwd)
SRC_DIR := $(ROOT_DIR)/src
PAPER_DIR := $(ROOT_DIR)/paper
TOOLS_DIR := $(ROOT_DIR)/tools

.PHONY: help doctor setup sims figs pdf all clean

help:
	@echo "Available targets:"
	@echo "  make doctor   - check environment"
	@echo "  make setup    - install python requirements"
	@echo "  make sims     - run all simulations"
	@echo "  make figs     - generate all figures"
	@echo "  make pdf      - build LaTeX paper"
	@echo "  make all      - sims + figs + pdf"
	@echo "  make clean    - remove build artifacts"

doctor:
	@bash $(TOOLS_DIR)/doctor.sh

setup:
	$(PIP) install -r requirements.txt

sims:
	@bash $(TOOLS_DIR)/run_sims.sh
		@echo "[5] Multi-seed exponent robustness"
	@$(PYTHON) -m src.sims.phi_scaling_multiseed
	@echo "[6] CTRW alpha sweep"
	@$(PYTHON) -m src.sims.ctrw_alpha_sweep
	@echo "[7] Ramsey optimal time under dephasing"
	@$(PYTHON) -m src.sims.ramsey_optimal_time_under_dephasing


figs:
	@$(PYTHON) -m src.figs.fig1_overview
	@$(PYTHON) -m src.figs.fig2_master_inequality_cartoon
	@$(PYTHON) -m src.figs.fig3_phi_scaling
	@$(PYTHON) -m src.figs.fig4_ou_gamma_bound
	@$(PYTHON) -m src.figs.fig5_ramsey_phase_diagram
	@$(PYTHON) -m src.figs.fig6_mzi_visibility
	@$(PYTHON) -m src.figs.fig7_noise_suppression_bound
		@$(PYTHON) -m src.figs.fig8_phi_slope_hist
	@$(PYTHON) -m src.figs.fig9_ctrw_alpha_sweep
	@$(PYTHON) -m src.figs.fig10_ramsey_optimal_time


pdf:
	@bash $(TOOLS_DIR)/build_pdf.sh

all: sims figs pdf

clean:
	@bash $(TOOLS_DIR)/clean.sh
