library(ComplexHeatmap)
library(openxlsx)
library(circlize)
setwd("C:/Lab/R studio/KIT")
#ktr<-read.xlsx('Pathways DNA and Cell cycle.xlsx')
#ktr<-read.xlsx('Pathways Kinases.xlsx')
ktr<-read.xlsx('Pathways GF.xlsx')
mat= as.matrix(ktr[-c(1:2),-1])
class(mat)<-"numeric"
rownames(mat) <- ktr[-c(1:2),1]
col_heat = colorRamp2(c(-15, -5, 0, 5, 15), c('#151e2a','#bbc9dc', "white", '#b86a79',"#890620"))
top<-as.character(ktr[2,-1])

ha = HeatmapAnnotation(
  day= as.character(ktr[1,-1]),
  col = list(day = c("day 3" = "#8A817C", "day 6" = "#FFD25A")),
  annotation_legend_param = list(title = "days"),
  annotation_label = 'days', annotation_name_gp= gpar(fontface="bold")
)

ht<-Heatmap(mat, top_annotation = ha, col=col_heat, 
            clustering_distance_rows = 'euclidean', cluster_columns = FALSE, clustering_method_rows = 'ward.D2', 
            show_row_names = TRUE, row_names_side = "left", show_column_names = FALSE, 
            column_dend_height = unit(1, "cm"), width = unit(4, "cm"), height = unit(10, "cm"),
            heatmap_legend_param = list(title = "PAS"), column_split = top
            )

draw(ht, merge_legend = TRUE)

c('#feebe2','#fbb4b9', '#f768a1', '#c51b8a', '#7a0177')
col = list(day = c("day 3" = "red", "day 6" = "green"))