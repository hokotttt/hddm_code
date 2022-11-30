%auWM_exp9_xierucsv

subj_idx=[];
    stim=[];
    rtt=[];
    response=[];
    rhythm=[];
    response1=[];
    response2=[];
    change_number=[];


%第1列：被试反应是否有变化（有变化：1 无变化：0）
%第2列：被试反应是否有变化是否正确（正确：1 不正确：0）
%第3列：被试反应是变高还是变低（变高：1 变低：0 没变：2）
%第4列：被试反应变高还是变低是否正确（正确：1 不正确：0）
%第5列：被试反应是否有变化反应时
%第6列：被试反应变高、变低反应时
sub=0;
for isub=1:25
    

sub=sub+1;
     if isub==15
        resp=[];
        for iblock=2:4
            load(sprintf('resp_sub%d_block%d',isub,iblock));
            resp=[resp;responsematrix];
            
        end
        load(sprintf('design_total_sub%d',isub));
        design_total=design_total(73:288,:);
    end
    
    if isub<15||isub>15
        
        resp=[];
        for iblock=1:4
            load(sprintf('resp_sub%d_block%d',isub,iblock));
            resp=[resp;responsematrix];
        end
        load(sprintf('design_total_sub%d',isub));
    end
    
    
    %加一列 53 变化了几个音
    for itrial=1:size(design_total,1)
        if design_total(itrial,13)==0
            design_total(itrial,53)=0;
        end
        
        if design_total(itrial,13)>0&&design_total(itrial,15)==0
            design_total(itrial,53)=2;
        end
        
        if design_total(itrial,16)>0
            design_total(itrial,53)=4;
        end
    end
    
% 
ind_good=find(resp(:,5)<10&resp(:,5)>0.15);
design_total=design_total(ind_good,:);% %删掉RT在0.15和10以上的试次
resp=resp(ind_good,:);

    
    
 %1-12 sequence
%13-16 change position
%17 change direction(1:higher 0:lower 2:no change)
%18-29 sequence after change
%30 rhythm(1:rhythmic 0:random)
%31-41 encoding SOA
%42-52 probeSOA
    
  design_total(find(design_total(:,17)==1|design_total(:,17)==0),17)=1;%发生变化，编码为1
    
    design_total(find(design_total(:,17)==2),17)=0;%没有发生变化，编码为0
   
   
    subj_idx=[subj_idx;sub*ones(size(design_total,1),1)];
    rhythm=[rhythm;design_total(:,30)];
   stim=[stim;design_total(:,17)];%真实刺激是否变化
    rtt=[rtt;resp(:,5)];%判断是否变化 反应时
    response1=[response1;resp(:,1)];%被试的真实选择：1：有变化 0：无变化
    response2=[response2;resp(:,2)];%选择是否正确 1：正确 0：不正确
    change_number=[change_number;design_total(:,53)];%变化了几个音
  
end
    
    
    columns = {'subj_idx','rhythm','response', 'stim', 'rt','change_number'};%stim:是否有节奏 response:被试的真实反应
data_exp9_change_stimuluscoding = table(subj_idx,rhythm,response1,stim, rtt,change_number,'VariableNames', columns);
writetable(data_exp9_change_stimuluscoding,'data_stimcoding_25_2.txt');

    
%     columns = {'subj_idx','rhythm','response', 'stim', 'rt','change_number'};%stim:是否有节奏 response:被试的真实反应
% data_exp9_change_accuracycoding = table(subj_idx,rhythm,response2,stim, rtt,change_number,'VariableNames', columns);
% writetable(data_exp9_change_accuracycoding,'data_exp9_change_accuracycoding_n=25.txt');