rm(list=ls())
library(vegan)
setwd('/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms')

dm_euclidean <- read.table("/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/distance_matrix_euclidean_asd_severity_sparse.tsv")

dm_hyperactivity = read.table("/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/scripted_dm_hyperactivity.txt")

dm_lethargy = read.table("/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/scripted_dm_lethargy.txt")
dm_weighted_unifrac <- read.table("/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/filtered_weighted_unifrac_distance_matrix_modified.tsv")

# print("THIS DOES NOT MAKE SENSE...")
# print(mantel(dm_euclidean, dm_weighted_unifrac, method = "pearson", permutations=999))
# print(mantel(dm_hyperactivity, dm_weighted_unifrac, method="pearson", permutations=999))
# print(mantel(dm_lethargy, dm_weighted_unifrac, method="pearson", permutations=999))

data_labels = c("12.1_12.2","14.1_14.2","14.1_14.3","14.2_14.3","22.1_22.2","22.1_22.3","22.1_22.4","22.2_22.3","22.2_22.4","22.3_22.4","24.1_24.2","27.2_27.4","27.2_27.5","27.4_27.5","6.2_6.4","7.1_7.2","7.1_7.3","7.1_7.4","7.2_7.3","7.2_7.4","7.3_7.4")
subjects = c("6", "7", "12", "14", "22", "24", "27")
colors = c("firebrick2", "blue3", "darkorchid", "coral", "forestgreen", "yellow2", "deeppink3")
irritability = c(10.0, 3.0, -2.0, -5.0, 0.0, 4.0, 6.0, 4.0, 6.0, 2.0, -8.0, 6.0, 8.0, 2.0, 4.0, -6.0, -10.0, -8.0, -4.0, -2.0, 2.0)
hyperactivity = c(7.0, 2.0, 0.0, -2.0, -4.0, 2.0, 9.0, 6.0, 13.0, 7.0, 7.0, 1.0, 2.0, 1.0, 5.0, -4.0, -1.0, -4.0, 3.0, 0.0, -3.0)
stereotypy = c(1.0, -1.0, 3.0, 4.0, 0.0, -1.0, 1.0, -1.0, 1.0, 2.0, -3.0, -2.0, -2.0, 0.0, 1.0, -2.0, -2.0, -2.0, 0.0, 0.0, 0.0)
inapp_speech = c(0.0, 2.0, 4.0, 2.0, 1.0, 1.0, 5.0, 0.0, 4.0, 4.0, -3.0, 2.0, 1.0, -1.0, 5.0, -2.0, -3.0, -2.0, -1.0, 0.0, 1.0)
lethargy = c(-1.0, -4.0, -1.0, 3.0, -6.0, -1.0, 0.0, 5.0, 6.0, 1.0, -2.0, 2.0, -6.0, -8.0, 11.0, 0.0, 1.0, 5.0, 1.0, 5.0, 4.0)
slurpee = c(-1.0, 0.0, 0.0, 0.0, -3.0, -3.0, -1.0, 0.0, 2.0, 2.0, 0.0, 0.0, 2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
euclidean = c(12.32882801, 5.567764363, 4.242640687, 7.416198487, 7.280109889, 5.099019514, 11.26942767, 8.888194417, 15.68438714, 7.681145748, 11.26942767, 6.782329983, 10.58300524, 8.366600265, 12.80624847, 7.549834435, 10.48808848, 10.86278049, 5.196152423, 5.744562647, 5.477225575)
weighted_unifrac = c(0.250405399, 0.143320292, 0.221448669, 0.300183276, 0.106750785, 0.28752638, 0.418629095, 0.301022682, 0.398150981, 0.210891019, 0.119843726, 0.099939122, 0.14175059, 0.089918009, 0.32273384, 0.092315999, 0.205174906, 0.191292454, 0.239619462, 0.252440368, 0.243502253)
unweighted_unifrac = c(0.288880109, 0.237725548, 0.219268979, 0.24665496, 0.264440053, 0.217830322, 0.255787332, 0.29526024, 0.292331925, 0.222636407, 0.213708084, 0.200344608, 0.228781456, 0.23661749, 0.303631262, 0.243386346, 0.300530476, 0.293815011, 0.263668155, 0.329244748, 0.285316192)

microbial_diversity_list = list(weighted_unifrac, unweighted_unifrac)
microbial_diversity_names_list = list("weighted_unifrac", "unweighted_unifrac")
severity_metric_list = list(irritability, hyperactivity, stereotypy, inapp_speech, lethargy, slurpee)
severity_names_list = list("irritability", "hyperactivity", "stereotypy", "inapp_speech", "lethargy", "slurpee")

print("WEIGHTED UNIFRAC CORRELATIONS")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
irritability_weighted_cor = cor.test(irritability, weighted_unifrac,  method = "pearson", use = "complete.obs")
hyperactivity_weighted_cor = cor.test(hyperactivity, weighted_unifrac,  method = "pearson", use = "complete.obs")
stereotypy_weighted_cor = cor.test(stereotypy, weighted_unifrac,  method = "pearson", use = "complete.obs")
inapp_speech_weighted_cor = cor.test(inapp_speech, weighted_unifrac,  method = "pearson", use = "complete.obs")
lethargy_weighted_cor = cor.test(lethargy, weighted_unifrac,  method = "pearson", use = "complete.obs")
slurpee_weighted_cor = cor.test(slurpee, weighted_unifrac,  method = "pearson", use = "complete.obs")
euclidean_weighted_cor = cor.test(euclidean, weighted_unifrac,  method = "pearson", use = "complete.obs")

print("irritability")
print(irritability_weighted_cor["p.value"])
print(irritability_weighted_cor["estimate"])
print("hyperactivity")
print(hyperactivity_weighted_cor["p.value"])
print(hyperactivity_weighted_cor["estimate"])
print("stereotypy")
print(stereotypy_weighted_cor["p.value"])
print(stereotypy_weighted_cor["estimate"])
print("inapp_speech")
print(inapp_speech_weighted_cor["p.value"])
print(inapp_speech_weighted_cor["estimate"])
print("lethargy")
print(lethargy_weighted_cor["p.value"])
print(lethargy_weighted_cor["estimate"])
print("slurpee")
print(slurpee_weighted_cor["p.value"])
print(slurpee_weighted_cor["estimate"])
print("euclidean")
print(euclidean_weighted_cor["p.value"])
print(euclidean_weighted_cor["estimate"])


print("UNWEIGHTED UNIFRAC CORRELATIONS")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
ir = cor.test(irritability, unweighted_unifrac,  method = "pearson", use = "complete.obs")
hyp = cor.test(hyperactivity, unweighted_unifrac,  method = "pearson", use = "complete.obs")
st = cor.test(stereotypy, unweighted_unifrac,  method = "pearson", use = "complete.obs")
inap = cor.test(inapp_speech, unweighted_unifrac,  method = "pearson", use = "complete.obs")
leth = cor.test(lethargy, unweighted_unifrac,  method = "pearson", use = "complete.obs")
sl = cor.test(slurpee, unweighted_unifrac,  method = "pearson", use = "complete.obs")
euc = cor.test(euclidean, unweighted_unifrac,  method = "pearson", use = "complete.obs")

print("irritability")
print(ir["p.value"])
print(ir["estimate"])
print("hyperactivity")
print(hyp["p.value"])
print(hyp["estimate"])
print("stereotypy")
print(st["p.value"])
print(st["estimate"])
print("inapp speech")
print(inap["p.value"])
print(inap["estimate"])
print("lethargy")
print(leth["p.value"])
print(leth["estimate"])
print("slurpee")
print(sl["p.value"])
print(sl["estimate"])
print("euclidean")
print(euc["p.value"])
print(euc["estimate"])


for (num in 1:length(severity_metric_list)) {
  severity_metric = severity_metric_list[num][[1]]
	for (metric_num in 1:length(microbial_diversity_list)) {
	  microbial_metric = microbial_diversity_list[metric_num][[1]]
	  pdf_name = paste0("severity_pdfs_", toString(microbial_diversity_names_list[metric_num]), "_", toString(severity_names_list[num]), ".pdf")
	  pdf(pdf_name)
		plot(severity_metric, microbial_metric, pch=19, xlab=toString(severity_names_list[num]), ylab=toString(microbial_diversity_names_list[metric_num]))
    abline(lm(microbial_metric ~ severity_metric), lwd=3)
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
          
          severity_values_for_subject = severity_metric[data_num][[1]]
          small_x_vector = c(small_x_vector, severity_values_for_subject)
          
          microbial_values_for_subject = microbial_metric[data_num][[1]]
          small_y_vector = c(small_y_vector, microbial_values_for_subject)
        }
      }
      # lines(small_x_vector, small_y_vector, col=subject_color, lwd=4)
      text(small_x_vector, small_y_vector, labels=data_labels_small, cex=0.8, pos=3, col=subject_color)
      try(abline(lm(small_y_vector ~ small_x_vector), col=subject_color, lwd=3), silent=TRUE)
    }
    dev.off()
	}
}


print(small_x_vector)

