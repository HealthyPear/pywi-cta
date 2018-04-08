#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Jérémie DECOCK (http://www.jdhp.org)

# This script is provided under the terms and conditions of the MIT license:
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

__all__ = []

import json
from scipy import optimize
from pywicta.optimization.objectivefunc.wavelets_mrfilter_delta_psi import ObjectiveFunction as WaveletMRFObjectiveFunction
from pywicta.optimization.objectivefunc.wavelets_mrtransform_delta_psi import ObjectiveFunction as WaveletMRTObjectiveFunction
from pywicta.optimization.objectivefunc.tailcut_delta_psi import ObjectiveFunction as TailcutObjectiveFunction

# For wavelets
import pywicta.denoising.cdf
from pywicta.denoising.inverse_transform_sampling import EmpiricalDistribution

def main():

    #algo = "wavelet_mrfilter"
    algo = "wavelet_mrtransform"
    #algo = "tailcut"

    #instrument = "ASTRICam"
    #instrument = "CHEC"
    #instrument = "DigiCam"
    #instrument = "FlashCam"
    #instrument = "NectarCam"
    instrument = "LSTCam"

    #max_num_img = None
    max_num_img = 500

    aggregation_method = "mean"
    #aggregation_method = "median"

    kill_islands = False

    print("algo:", algo)
    print("instrument:", instrument)
    print("kill_islands:", kill_islands)

    if instrument == "ASTRICam":

        input_files = ["/dev/shm/.jd/astri/gamma/"]
        noise_distribution = EmpiricalDistribution(pywicta.denoising.cdf.ASTRI_CDF_FILE)

        if algo == "wavelet_mrfilter":
            search_ranges = (slice(1, 5, 1),           # Scale 0 (smallest scale)
                             slice(1, 5, 1),           # Scale 1
                             slice(1, 5, 1),           # Scale 2
                             slice(1, 5, 1))           # Scale 3 (largest scale)
        elif algo == "wavelet_mrtransform":
            search_ranges = (slice(1, 5, 1),           # Scale 0 (smallest scale)
                             slice(1, 5, 1),           # Scale 1
                             slice(1, 5, 1),           # Scale 2
                             slice(1, 5, 1))           # Scale 3 (largest scale)
        elif algo == "tailcut":
            search_ranges = (slice(-2., 10., 0.5),     # Core threshold (largest threshold)
                             slice(-2., 10., 0.5))     # Boundary threshold (smallest threshold)

    elif instrument == "CHEC":

        input_files = ["/dev/shm/.jd/gct/gamma/"]
        noise_distribution = EmpiricalDistribution(pywicta.denoising.cdf.GCT_CDF_FILE)

        if algo == "wavelet_mrfilter":
            search_ranges = (slice(1, 5, 1),           # Scale 0 (smallest scale)
                             slice(1, 5, 1),           # Scale 1
                             slice(1, 5, 1),           # Scale 2
                             slice(1, 5, 1))           # Scale 3 (largest scale)
        elif algo == "wavelet_mrtransform":
            search_ranges = (slice(1, 5, 1),           # Scale 0 (smallest scale)
                             slice(1, 5, 1),           # Scale 1
                             slice(1, 5, 1),           # Scale 2
                             slice(1, 5, 1))           # Scale 3 (largest scale)
        elif algo == "tailcut":
            search_ranges = (slice(-2., 10., 0.5),     # Core threshold (largest threshold)
                             slice(-2., 10., 0.5))     # Boundary threshold (smallest threshold)

    elif instrument == "DigiCam":

        input_files = ["/dev/shm/.jd/digicam/gamma/"]
        noise_distribution = EmpiricalDistribution(pywicta.denoising.cdf.DIGICAM_CDF_FILE)

        if algo == "wavelet_mrfilter":
            search_ranges = (slice(1, 5, 1),           # Scale 0 (smallest scale)
                             slice(1, 5, 1),           # Scale 1
                             slice(1, 5, 1),           # Scale 2
                             slice(1, 5, 1))           # Scale 3 (largest scale)
        elif algo == "wavelet_mrtransform":
            search_ranges = (slice(1, 5, 1),           # Scale 0 (smallest scale)
                             slice(1, 5, 1),           # Scale 1
                             slice(1, 5, 1),           # Scale 2
                             slice(1, 5, 1))           # Scale 3 (largest scale)
        elif algo == "tailcut":
            search_ranges = (slice(-2., 10., 0.5),     # Core threshold (largest threshold)
                             slice(-2., 10., 0.5))     # Boundary threshold (smallest threshold)

    elif instrument == "FlashCam":

        input_files = ["/dev/shm/.jd/flashcam/gamma/"]
        noise_distribution = EmpiricalDistribution(pywicta.denoising.cdf.FLASHCAM_CDF_FILE)

        if algo == "wavelet_mrfilter":
            search_ranges = (slice(1, 5, 1),           # Scale 0 (smallest scale)
                             slice(1, 5, 1),           # Scale 1
                             slice(1, 5, 1),           # Scale 2
                             slice(1, 5, 1))           # Scale 3 (largest scale)
        elif algo == "wavelet_mrtransform":
            search_ranges = (slice(1, 5, 1),           # Scale 0 (smallest scale)
                             slice(1, 5, 1),           # Scale 1
                             slice(1, 5, 1),           # Scale 2
                             slice(1, 5, 1))           # Scale 3 (largest scale)
        elif algo == "tailcut":
            search_ranges = (slice(-2., 10., 0.5),     # Core threshold (largest threshold)
                             slice(-2., 10., 0.5))     # Boundary threshold (smallest threshold)

    elif instrument == "NectarCam":

        input_files = ["/dev/shm/.jd/nectarcam/gamma/"]
        noise_distribution = EmpiricalDistribution(pywicta.denoising.cdf.NECTARCAM_CDF_FILE)

        if algo == "wavelet_mrfilter":
            search_ranges = (slice(1, 5, 1),           # Scale 0 (smallest scale)
                             slice(1, 5, 1),           # Scale 1
                             slice(1, 5, 1),           # Scale 2
                             slice(1, 5, 1))           # Scale 3 (largest scale)
        elif algo == "wavelet_mrtransform":
            search_ranges = (slice(1, 5, 1),           # Scale 0 (smallest scale)
                             slice(1, 5, 1),           # Scale 1
                             slice(1, 5, 1),           # Scale 2
                             slice(1, 5, 1))           # Scale 3 (largest scale)
        elif algo == "tailcut":
            search_ranges = (slice(-2., 10., 0.5),     # Core threshold (largest threshold)
                             slice(-2., 10., 0.5))     # Boundary threshold (smallest threshold)

    elif instrument == "LSTCam":

        input_files = ["/dev/shm/.jd/lstcam/gamma/lst_faint/"]
        #input_files = ["~/data/grid_prod3b_north/simtel/gamma"]
        noise_distribution = EmpiricalDistribution(pywicta.denoising.cdf.LSTCAM_CDF_FILE)

        if algo == "wavelet_mrfilter":
            search_ranges = (slice(1., 14., 1.),      # Scale 0 (smallest scale)
                             slice(1., 9.,  1.),      # Scale 1
                             slice(1., 6.,  1.))      # Scale 3 (largest scale aside residuals)
        elif algo == "wavelet_mrtransform":
            search_ranges = (slice(0., 15., 1.),      # Scale 0 (smallest scale)
                             slice(0., 2.,  0.5))     # Scale 1 (largest scale aside residuals)
        elif algo == "tailcut":
            search_ranges = (slice(1., 10., 0.5),     # Core threshold (largest threshold)
                             slice(1., 10., 0.5))     # Boundary threshold (smallest threshold)

    else:

        raise Exception("Unknown instrument", instrument)

    print("input_files:", input_files)
    print("noise_distribution:", noise_distribution.cdf_json_file_path)

    if algo == "wavelet_mrfilter":

        func = WaveletMRFObjectiveFunction(input_files=input_files,
                                           cam_id=instrument,
                                           noise_distribution=noise_distribution,
                                           max_num_img=max_num_img,
                                           aggregation_method=aggregation_method,  # "mean" or "median"
                                           kill_isolated_pixels=kill_islands)

    elif algo == "wavelet_mrtransform":

        func = WaveletMRTObjectiveFunction(input_files=input_files,
                                           cam_id=instrument,
                                           noise_distribution=noise_distribution,
                                           max_num_img=max_num_img,
                                           aggregation_method=aggregation_method,  # "mean" or "median"
                                           kill_isolated_pixels=kill_islands)

    elif algo == "tailcut":

        func = TailcutObjectiveFunction(input_files=input_files,
                                        cam_id=instrument,
                                        max_num_img=max_num_img,
                                        aggregation_method=aggregation_method,  # "mean" or "median"
                                        kill_isolated_pixels=kill_islands)

    else:

        raise ValueError("Unknown algorithm", algo)

    res = optimize.brute(func,
                         search_ranges,
                         full_output=True,
                         finish=None)     #optimize.fmin)

    print("x* =", res[0])
    print("f(x*) =", res[1])

    # SAVE RESULTS ############################################################

    res_dict = {
                "best_solution": res[0].tolist(),
                "best_score": float(res[1]),
                "solutions": res[2].tolist(),
                "scores": res[3].tolist()
               }

    with open("optimize_sigma.json", "w") as fd:
        json.dump(res_dict, fd, sort_keys=True, indent=4)  # pretty print format


if __name__ == "__main__":
    main()
