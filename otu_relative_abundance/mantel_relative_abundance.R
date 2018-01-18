rm(list=ls())
library(vegan)
library(rio)
args = commandArgs(trailingOnly=TRUE)
options(scipen = 999)

# setwd('/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/otu_relative_abundance')

diet = c(10.48808848,8.717797887,9.695359715,8.124038405,10.14889157,12.16552506,11.26942767,10.04987562,10.95445115,10.34408043,13.07669683,11.40175425,14.24780685,15.13274595,13.19090596,12.08304597,8.366600265,9.38083152,14.14213562,13.56465997,6.92820323)
euclidean = c(12.28820573,5.830951895,5.477225575,7.615773106,7.280109889,4.795831523,11.95826074,8.831760866,16.0623784,8.602325267,11.61895004,7,10.44030651,8.366600265,13.7113092,7.745966692,10.72380529,10.63014581,5.196152423,5.385164807,5.477225575)

weighted_unifrac = c(0.250405399, 0.143320292, 0.221448669, 0.300183276, 0.106750785, 0.28752638, 0.418629095, 0.301022682, 0.398150981, 0.210891019, 0.119843726, 0.099939122, 0.14175059, 0.089918009, 0.32273384, 0.092315999, 0.205174906, 0.191292454, 0.239619462, 0.252440368, 0.243502253)
unweighted_unifrac = c(0.288880109, 0.237725548, 0.219268979, 0.24665496, 0.264440053, 0.217830322, 0.255787332, 0.29526024, 0.292331925, 0.222636407, 0.213708084, 0.200344608, 0.228781456, 0.23661749, 0.303631262, 0.243386346, 0.300530476, 0.293815011, 0.263668155, 0.329244748, 0.285316192)

data_labels = c("12.1_12.2","14.1_14.2","14.1_14.3","14.2_14.3","22.1_22.2","22.1_22.3","22.1_22.4","22.2_22.3","22.2_22.4","22.3_22.4","24.1_24.2","27.2_27.4","27.2_27.5","27.4_27.5","6.2_6.4","7.1_7.2","7.1_7.3","7.1_7.4","7.2_7.3","7.2_7.4","7.3_7.4")
subjects = c("6", "7", "12", "14", "22", "24", "27")
colors = c("firebrick2", "blue3", "darkorchid", "coral", "forestgreen", "yellow2", "deeppink3")

create_graphs = function(severity_metric_file, otu_file){

  severity_metric_file = import(severity_metric_file)
  otu_abundance_file = import(otu_file)

  for (sev in 1:length(severity_metric_file)){

    # value lists for each severity metric
    p_values = c()
    asv_list = c()
    r_list = c()

    for (num in 1:length(otu_abundance_file)) {

      correlation_test = ""
      otu_metric = otu_abundance_file[num][[1]]
      severity_metric_final = severity_metric_file[sev][[1]]
      correlation_test = cor.test(otu_metric, severity_metric_final,  method = "pearson", use = "complete.obs")
      p = as.numeric(correlation_test$p.value)
      r = as.numeric(correlation_test$estimate)

      if (toString(p) == 'NA'){
        next
      }
      vals = table(otu_metric)
      num_zeros_in_metric_list = as.numeric(vals[names(vals)==0])

      if (length(num_zeros_in_metric_list) == 0 ){
        # no zeros in metric
      }
      else if (num_zeros_in_metric_list > 10){
        # 21-10 = 11 comparisons required
        next
      }

      p_values = c(p_values, p)
      asv_list = c(asv_list, toString(names(otu_abundance_file[num])))
      r_list = c(r_list, r)

      if (p > 0.01){
        next
      }

      pdf_name = paste0("severitypdfs_", toString(names(severity_metric_file[sev])), '_', toString(names(otu_abundance_file[num])), '_', round(p, digits=5), '_', round(r, digits=2), ".pdf")
      pdf(pdf_name)
      plot(otu_metric, severity_metric_final, pch=19, xlab=toString(names(otu_abundance_file[num])), ylab=toString(names(severity_metric_file[sev])))
      try(abline(lm(severity_metric_final ~ severity_metric), lwd=3), silent=TRUE)
      for (subject_num in 1:length(subjects)) {
        subject = subjects[subject_num][[1]]
        small_x_vector = numeric()
        small_y_vector = numeric()
        data_labels_small = c()
        subject_color = colors[subject_num][[1]]
        for (data_num in 1:length(data_labels)){
          data_label = data_labels[data_num][[1]]
          if (startsWith(data_label, subject)) {
            data_labels_small = c(data_labels_small, data_label)

            severity_values_for_subject = otu_metric[data_num][[1]]
            small_x_vector = c(small_x_vector, severity_values_for_subject)

            microbial_values_for_subject = severity_metric_final[data_num][[1]]
            small_y_vector = c(small_y_vector, microbial_values_for_subject)
          }
        }
        text(small_x_vector, small_y_vector, labels=data_labels_small, cex=0.8, pos=3, col=subject_color)
        try(abline(lm(small_y_vector ~ small_x_vector), col=subject_color, lwd=3), silent=TRUE)
      }
      dev.off()
    }

    p_values_adjusted = p.adjust(p_values, method="fdr", n=length(p_values))
    print(toString(r_list))
    print(toString(p_values))
    print(toString(p_values_adjusted))
    print(toString(asv_list))
  }
}

create_graphs(args[1], args[2])
