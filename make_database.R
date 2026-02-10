

library(dplyr)
setwd("C:/Users/sjeng/OneDrive - The University of Texas at Austin/Coding/Music_Display/playlist_files/")

add_to_dataframe <- function(){
    first <- read.csv(files_list[1], stringsAsFactors = F)
    first$Playlist <- sub("\\.csv$", "", files_list[1])
    data_frame_buffer <- first
    
    for (filename in files_list[-1]){  
        subfile <- read.csv(filename, stringsAsFactors = F)
        playlist_name <- gsub(x = filename, 
                              pattern = "\\.csv",
                              replacement = "")
        subfile$Playlist <- playlist_name
        data_frame_buffer <- bind_rows(x = data_frame_buffer, 
                                       y = subfile)
    }
    return(data_frame_buffer)
}

all_data <- add_to_dataframe()

write.csv(all_data, "all_data.csv", row.names = F)