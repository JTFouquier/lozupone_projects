rm(list=ls())
library(vegan)
setwd('/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms')

dm_euclidean <- read.table("/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/euclidean_dm_asd_severity_112817_sparse.txt")
dm_hyperactivity = read.table("/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/scripted_dm_hyperactivity.txt")
dm_lethargy = read.table("/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/scripted_dm_lethargy.txt")
dm_weighted_unifrac <- read.table("/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/filtered_weighted_unifrac_distance_matrix_modified.tsv")


complete_weighted_unifrac_dm = read.table("/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/filtered_weighted_unifrac_distance_matrix.tsv")
complete_euclidean_diet_dm = read.table("/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/euclidean_dm_diet.txt")
complete_euclidean_severity_dm = read.table("/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/euclidean_dm_asd_severity_112817.txt")

diet = c(10.48808848,8.717797887,9.695359715,8.124038405,10.14889157,12.16552506,11.26942767,10.04987562,10.95445115,10.34408043,13.07669683,11.40175425,14.24780685,15.13274595,13.19090596,12.08304597,8.366600265,9.38083152,14.14213562,13.56465997,6.92820323)
euclidean = c(12.28820573,5.830951895,5.477225575,7.615773106,7.280109889,4.795831523,11.95826074,8.831760866,16.0623784,8.602325267,11.61895004,7,10.44030651,8.366600265,13.7113092,7.745966692,10.72380529,10.63014581,5.196152423,5.385164807,5.477225575)
# error in this euclidean
# euclidean = c(12.32882801, 5.567764363, 4.242640687, 7.416198487, 7.280109889, 5.099019514, 11.26942767, 8.888194417, 15.68438714, 7.681145748, 11.26942767, 6.782329983, 10.58300524, 8.366600265, 12.80624847, 7.549834435, 10.48808848, 10.86278049, 5.196152423, 5.744562647, 5.477225575)
weighted_unifrac = c(0.250405399, 0.143320292, 0.221448669, 0.300183276, 0.106750785, 0.28752638, 0.418629095, 0.301022682, 0.398150981, 0.210891019, 0.119843726, 0.099939122, 0.14175059, 0.089918009, 0.32273384, 0.092315999, 0.205174906, 0.191292454, 0.239619462, 0.252440368, 0.243502253)
unweighted_unifrac = c(0.288880109, 0.237725548, 0.219268979, 0.24665496, 0.264440053, 0.217830322, 0.255787332, 0.29526024, 0.292331925, 0.222636407, 0.213708084, 0.200344608, 0.228781456, 0.23661749, 0.303631262, 0.243386346, 0.300530476, 0.293815011, 0.263668155, 0.329244748, 0.285316192)

# print("THIS DOES NOT MAKE SENSE...")
print(mantel(dm_euclidean, dm_weighted_unifrac, method = "pearson", permutations=999))
# print(mantel(dm_hyperactivity, dm_weighted_unifrac, method="pearson", permutations=999))
# print(mantel(dm_lethargy, dm_weighted_unifrac, method="pearson", permutations=999))

data_labels = c("12.1_12.2","14.1_14.2","14.1_14.3","14.2_14.3","22.1_22.2","22.1_22.3","22.1_22.4","22.2_22.3","22.2_22.4","22.3_22.4","24.1_24.2","27.2_27.4","27.2_27.5","27.4_27.5","6.2_6.4","7.1_7.2","7.1_7.3","7.1_7.4","7.2_7.3","7.2_7.4","7.3_7.4")
subjects = c("6", "7", "12", "14", "22", "24", "27")
colors = c("firebrick2", "blue3", "darkorchid", "coral", "forestgreen", "yellow2", "deeppink3")

library(rio)
test = import("/Volumes/JEN_DATA/autism_project/microbial_analysis/03_mapping/updated_mappings_110917/mapping_asd_dms/vectors_for_r_graphs.tsv")

microbial_diversity_list = list(weighted_unifrac, unweighted_unifrac)
microbial_diversity_names_list = list("weighted_unifrac", "unweighted_unifrac")

for (i in 1:length(names(test))) {
  for (uni in microbial_diversity_list){
    correlation_test = cor.test(test[i][[1]], uni,  method = "pearson", use = "complete.obs")
    print(names(test[i]))
    print(correlation_test$p.value)
    print(correlation_test$estimate)
  }
}

# # create graphs with vectors for each metric
# for (num in 1:length(test)) {
#   severity_metric = test[num][[1]]
# 	for (metric_num in 1:length(microbial_diversity_list)) {
# 	  microbial_metric = microbial_diversity_list[metric_num][[1]]
# 	  pdf_name = paste0("severity_pdfs_", toString(microbial_diversity_names_list[metric_num]), "_", toString(names(test[num])), ".pdf")
# 	  pdf(pdf_name)
# 		plot(severity_metric, microbial_metric, pch=19, xlab=toString(names(test[num])), ylab=toString(microbial_diversity_names_list[metric_num]))
# 		try(abline(lm(microbial_metric ~ severity_metric), lwd=3), silent=TRUE)
# 		# abline(lm(microbial_metric ~ severity_metric), lwd=3)
#     for (subject_num in 1:length(subjects)) {
#       subject = subjects[subject_num][[1]]
#       small_x_vector = numeric()
#       small_y_vector = numeric()
#       data_labels_small = c()
#       subject_color = colors[subject_num][[1]]
#       for (data_num in 1:length(data_labels)){
#         data_label = data_labels[data_num][[1]]
#         if (startsWith(data_label, subject)) {
#           data_labels_small = c(data_labels_small, data_label)
# 
#           severity_values_for_subject = severity_metric[data_num][[1]]
#           small_x_vector = c(small_x_vector, severity_values_for_subject)
# 
#           microbial_values_for_subject = microbial_metric[data_num][[1]]
#           small_y_vector = c(small_y_vector, microbial_values_for_subject)
#         }
#       }
#       # lines(small_x_vector, small_y_vector, col=subject_color, lwd=4)
#       text(small_x_vector, small_y_vector, labels=data_labels_small, cex=0.8, pos=3, col=subject_color)
#       try(abline(lm(small_y_vector ~ small_x_vector), col=subject_color, lwd=3), silent=TRUE)
#     }
#     dev.off()
# 	}
# }

# create graphs with vectors for each metric
severity_metric = diet
microbial_metric = weighted_unifrac
pdf_name = paste0("pdf_diet_euclidean_vector_weighted_unifrac.pdf")
pdf(pdf_name)
plot(severity_metric, microbial_metric, pch=19, xlab="Diet Euclidean Distance", ylab="Weighted UniFrac Distance")
try(abline(lm(microbial_metric ~ severity_metric), lwd=3), silent=TRUE)
# abline(lm(microbial_metric ~ severity_metric), lwd=3)
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
  text(small_x_vector, small_y_vector, labels=data_labels_small, cex=0.8, pos=3, col=subject_color)
  try(abline(lm(small_y_vector ~ small_x_vector), col=subject_color, lwd=3), silent=TRUE)
}
dev.off()

severity_metric = diet
microbial_metric = unweighted_unifrac
pdf_name = paste0("pdf_diet_euclidean_vector_unweighted_unifrac.pdf")
pdf(pdf_name)
plot(severity_metric, microbial_metric, pch=19, xlab="Diet Euclidean Distance", ylab="Unweighted UniFrac Distance")
try(abline(lm(microbial_metric ~ severity_metric), lwd=3), silent=TRUE)
# abline(lm(microbial_metric ~ severity_metric), lwd=3)
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
  text(small_x_vector, small_y_vector, labels=data_labels_small, cex=0.8, pos=3, col=subject_color)
  try(abline(lm(small_y_vector ~ small_x_vector), col=subject_color, lwd=3), silent=TRUE)
}
dev.off()

# create graphs with vectors for each metric
severity_metric = euclidean
microbial_metric = weighted_unifrac
pdf_name = paste0("pdf_severity_euclidean_vector_weighted_unifrac.pdf")
pdf(pdf_name)
plot(severity_metric, microbial_metric, pch=19, xlab="ASD Severity Euclidean Distance", ylab="Weighted UniFrac Distance")
try(abline(lm(microbial_metric ~ severity_metric), lwd=3), silent=TRUE)
# abline(lm(microbial_metric ~ severity_metric), lwd=3)
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
  text(small_x_vector, small_y_vector, labels=data_labels_small, cex=0.8, pos=3, col=subject_color)
  try(abline(lm(small_y_vector ~ small_x_vector), col=subject_color, lwd=3), silent=TRUE)
}
dev.off()

severity_metric = euclidean
microbial_metric = unweighted_unifrac
pdf_name = paste0("pdf_severity_euclidean_vector_unweighted_unifrac.pdf")
pdf(pdf_name)
plot(severity_metric, microbial_metric, pch=19, xlab="ASD Severity Euclidean Distance", ylab="Unweighted UniFrac Distance")
try(abline(lm(microbial_metric ~ severity_metric), lwd=3), silent=TRUE)
# abline(lm(microbial_metric ~ severity_metric), lwd=3)
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
  text(small_x_vector, small_y_vector, labels=data_labels_small, cex=0.8, pos=3, col=subject_color)
  try(abline(lm(small_y_vector ~ small_x_vector), col=subject_color, lwd=3), silent=TRUE)
}
dev.off()



correlation_test = mantel(dm_euclidean, dm_weighted_unifrac,  method = "pearson")
print(correlation_test)

correlation_test = cor.test(euclidean, weighted_unifrac,  method = "pearson", use = "complete.obs")
print(correlation_test)

correlation_test = cor.test(euclidean, unweighted_unifrac,  method = "pearson", use = "complete.obs")
print(correlation_test)


correlation_test = cor.test(diet, weighted_unifrac,  method = "pearson", use = "complete.obs")
print(correlation_test)

correlation_test = cor.test(diet, unweighted_unifrac,  method = "pearson", use = "complete.obs")
print(correlation_test)


print(mantel(complete_weighted_unifrac_dm, complete_euclidean_diet_dm, method = "pearson", permutations=999))
print(mantel(complete_weighted_unifrac_dm, complete_euclidean_severity_dm, method = "pearson", permutations=999))

