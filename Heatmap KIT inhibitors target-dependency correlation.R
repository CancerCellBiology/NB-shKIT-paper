library(ComplexHeatmap)
library(openxlsx)
library(circlize)
setwd("C:/Lab/R studio/KIT")
ktr<-read.xlsx('KIT inhibitors targets deps AUC correlation.xlsx')
mat= as.matrix(ktr[-1,-1])
class(mat)<-"numeric"
rownames(mat) <- ktr[-1,1]
col_heat = colorRamp2(c(-0.6, -0.3, 0, 0.3, 0.6), c('#151e2a','#bbc9dc', "white", '#b86a79',"#890620"))

col_fun = colorRamp2(c(-0.6, -0.3, 0, 0.3, 0.6), c('#151e2a','#bbc9dc', "white", '#b86a79',"#890620"))
scores<- as.vector(ktr[1,-1])
class(scores)<-"numeric"
ha = HeatmapAnnotation(
  score= scores,
  col = list(score = col_fun),
  annotation_legend_param = list(title = "mean"),
  annotation_label = 'Mean correlation', annotation_name_gp= gpar(fontface="bold"),
  show_legend = c(FALSE)
)

ht<-Heatmap(mat, top_annotation = ha, name = "Pearson correlation", col=col_heat, 
            cluster_columns = FALSE, clustering_method_rows = 'ward.D2', 
            show_row_names = TRUE, row_names_side = "left", show_column_names = TRUE, 
            show_column_dend = FALSE, show_row_dend = FALSE,
            column_names_side = "top", column_dend_height = unit(1, "cm"), width = unit(8, "cm"), height = unit(6, "cm"),
            heatmap_legend_param = list(title = "Correlation \ncoefficient")
)


draw(ht, merge_legend = TRUE)

c('#feebe2','#fbb4b9', '#f768a1', '#c51b8a', '#7a0177')