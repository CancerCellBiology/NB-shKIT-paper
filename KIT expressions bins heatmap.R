library(ComplexHeatmap)
library(openxlsx)
library(circlize)
library(RColorBrewer)
setwd("C:/Lab/R studio/KIT")
ktr<-read.xlsx('R2_datsets_KIT_tumors_distribution.xlsx')
mat= as.matrix(ktr[-1,-1])
class(mat)<-"numeric"
rownames(mat) <- ktr[-1,1]


densityHeatmap(mat, title = "KIT expression distribution", ylab = "log2 expression",
               cluster_columns = TRUE, clustering_distance_columns = "euclidean", clustering_method_columns= 'ward.D2',
              heatmap_legend_param = list(title = "Distribution /ndensity"))

densityHeatmap(mat, title = "KIT expression distribution", ylab = "log2 expression",
               cluster_columns = TRUE, clustering_distance_columns = "ks", 
               heatmap_legend_param = list(title = "Distribution \ndensity, %"),
               column_names_side = "top", width = unit(15, "cm"), height = unit(10, "cm"))

col = rev(RColorBrewer::brewer.pal(5,"RdGy"))