jQuery.aaSC=new function(){this.prefix="aaSC_Control";this.aaSCArray=function(aaSCField){var controlMatch=new RegExp(jQuery.aaSC.prefix+".*?(?=\\s)");var controlClass=(aaSCField.className+" ").match(controlMatch);var p=controlClass[0].split("_");this.role=p[1];this.groupName=p[2];this.status=p[3];this.effect=p[4];this.type=aaSCField.type;};this.reset=function(){jQuery("[class*=aaSC_Target]").removeAttr("disabled").removeClass("disabled").datepicker("enable").css("visibility","visible").show();};this.applyControlRules=function(a,type){jQuery(".aaSC_Target_"+a.groupName+"_"+a.status+"_Disable").addClass("disabled").attr("disabled","disabled").datepicker("disable");jQuery(".aaSC_Target_"+a.groupName+"_"+a.status+"_Hide").hide();jQuery(".aaSC_Target_"+a.groupName+"_"+a.status+"_MakeInvisible").css("visibility","hidden");if(a.type=="checkbox"){jQuery(".aaSC_Target_"+a.groupName+"_"+a.status+"_Show").removeAttr("disabled").removeClass("disabled").css("visibility","visible").show();}};this.update=function(event){jQuery.aaSC.reset();jQuery("input[class*="+jQuery.aaSC.prefix+"][type=radio]:checked").each(function(){jQuery.aaSC.applyControlRules(new jQuery.aaSC.aaSCArray(this));});jQuery("input[class*="+jQuery.aaSC.prefix+"][type=checkbox]:checked").each(function(){jQuery.aaSC.applyControlRules(new jQuery.aaSC.aaSCArray(this));});jQuery("select[class*="+jQuery.aaSC.prefix+"]").each(function(){jQuery(this).children(":selected").each(function(){jQuery.aaSC.applyControlRules(new jQuery.aaSC.aaSCArray(this));});});if(event!==null){jQuery("a[class*="+jQuery.aaSC.prefix+"]").each(function(){jQuery.aaSC.applyControlRules(new jQuery.aaSC.aaSCArray(this));});}};this.flag=function(message,direction,target){var t=jQuery(target);var flag=jQuery('<div class="aa-flag" style="display: none;"><div class="aa-flag-pointer"></div><div class="aa-flag-content"></div><a class="aa-flag-close" href="#" title="Close this panel">X</a></div>');if(direction=="left"){jQuery(".aa-flag-pointer",flag).addClass("aa-flag-pointer-left");}else{jQuery(".aa-flag-pointer",flag).addClass("aa-flag-pointer-right");}jQuery(".aa-flag-content",flag).html(message);jQuery(".aa-flag-close",flag).click(function(e){e.preventDefault();flag.hide().remove();});flag.appendTo(t).css("left",t.outerWidth()+20).css("z-index","99999").show();};};jQuery.fn.aaSC=function(dropDownValues){jQuery("input[class*="+jQuery.aaSC.prefix+"]").click(jQuery.aaSC.update);jQuery("a[class*="+jQuery.aaSC.prefix+"]").click(jQuery.aaSC.update);jQuery("select[class*="+jQuery.aaSC.prefix+"]").change(jQuery.aaSC.update).each(function(){var controlMatch=new RegExp(jQuery.aaSC.prefix+".*?(?=\\s)");var controlClass=(this.className+" ").match(controlMatch);jQuery(this).children().each(function(){var value=null;if(dropDownValues){value=dropDownValues(controlClass,this.value);}if(value){value=controlClass+"_"+value;}else{value=controlClass+"_"+this.value.replace(" ","_");}this.className=value;});});jQuery.aaSC.update(null);};