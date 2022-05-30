library(ComplexHeatmap)
library(openxlsx)
library(circlize)
setwd("C:/Lab/R studio/KIT")
ktr<-read.xlsx('Immune_sig_corr_KIT_R2_tumors_R-values.xlsx')
mat= as.matrix(ktr[-1,-1])
class(mat)<-"numeric"
rownames(mat) <- ktr[-1,1]
col_heat = colorRamp2(c(-0.5, -0.25, 0, 0.25, 0.5), c('#151e2a','#bbc9dc', "white", '#b86a79',"#890620"))

col_fun = colorRamp2(c(0, 5, 10, 15, 20), c('#f1eef6','#d7b5d8', '#df65b0', '#dd1c77', '#980043'))
scores<- as.vector(ktr[1,-1])
class(scores)<-"numeric"
ha = HeatmapAnnotation(
  score= scores,
  col = list(score = col_fun),
  annotation_legend_param = list(title = "Number of \ncorrelations"),
  annotation_label = 'Significant correlations', annotation_name_gp= gpar(fontface="bold")
  )

ht<-Heatmap(mat, top_annotation = ha, name = "Pearson correlation", col=col_heat, 
        clustering_distance_rows = 'euclidean', clustering_method_columns= 'ward.D2', clustering_method_rows = 'ward.D2', 
        show_row_names = TRUE, row_names_side = "left", show_column_names = TRUE, column_names_side = "top", 
        column_dend_height = unit(1, "cm"), width = unit(8, "cm"), height = unit(12, "cm"),
        heatmap_legend_param = list(title = "Correlation \ncoefficient")
        )


draw(ht, merge_legend = TRUE)

c('#feebe2','#fbb4b9', '#f768a1', '#c51b8a', '#7a0177')