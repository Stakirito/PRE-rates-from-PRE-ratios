# PRE-rates-from-PRE-ratios
Calculate PRE rates from PRE ratios for NMR data at different buffer conditions

This script should be used as follows:
reformat_ccpn_ttn_formula_pre_r2.py q558c_ratio_simple q558c_hydrogen_width_simple.txt > rp_tmp

q558c_ratio_simple contains information about measured PRE rates, each column is PRE rates for different residues at particular condition
q558c_hydrogen_width_simple.txt contains information about hydrogen widths, values shoule be stored in the same order as it was done for PRE ratios

This is a script, which allows to calculate PRE ratios from PRE rates, which were measured as an intensity ratio of paramagnetic to diamagnetic sample.
PRE ratios are related to PRE rates:
r = r2*np.exp(-10.6/1000*rp)/(r2+rp), where r is ratio, r2 is hydrogen width in Hz, rp is the PRE rate.
Script takes each value of r and r2 from the files and calculates rp.
