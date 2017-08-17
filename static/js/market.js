$(function(){
	//阻止冒泡
	$(".sosobtc-item .row-name a").click(function(event){
		event.stopPropagation();
	});
	//跳转至K线
	$(".sosobtc-item table").delegate("tr", "click", function(){
		if ($(this).data("hide") == "0"){
			window.open('https://k.sosobtc.com/' + $(this).data("type") + '_' + $(this).data("id") + '.html');
		}
	});
	//刷新数据
	(function(){
		var trList = $(".sosobtc-item tr"),
			param  = (function(){
				var tmp = [];
				trList.each(function(){
					tmp.push($(this).data("type") + ":" + $(this).data("id"));
				});
				return encodeURIComponent(tmp.join("|"));
			})();
		
		//底部时间
		var bottomTime = (function(){
			var loop = null;
			function start(){
				if ($(".text-tip").length == 0) return ;
				loop = setInterval(function(){
					$(".text-tip font").text(parseInt($(".text-tip font").text()) + 1);
				}, 1000);
			}
			
			function stop(){
				clearInterval(loop);
			}
			
			function restart(){
				stop();
				$(".text-tip font").text("0");
				start();
			}
			
			return {
				start   : start,
				stop    : stop, 
				restart : restart
			};
		})();
		
		setInterval(function(){
			$.get("//plugin-tickers.sosobtc.com/direct/plugin_market?sid=" + encodeURIComponent(sid) + "&list=" + param, function(data){
				//请求失败
				if (data.success == 0) return ;
				//遍历元素更改价格
				trList.each(function(){
					var key, row, priceWrap = $(this).find(".row-price");
					key = $(this).data("type") + "_" + $(this).data("id");
					if (data.list[key]){
						row = data.list[key];
						//最新价格
						if (priceWrap.length != 0){
							if (row.currency == "2"){
								$(this).find(".last-usd font").text(row.last);
								$(this).find(".last-cny font").text((row.last * data.rate).toFixed(2));
							}else{
								$(this).find(".last-cny font").text(row.last);
								//兼容山寨币
								if ($(this).find(".last-usd").length != 0){
									$(this).find(".last-usd font").text((row.last / data.rate).toFixed(2));
								}
							}
							
							if (priceWrap.data("price") < row.last){
								priceWrap.removeClass("data-down").addClass("data-up");
							}else if (priceWrap.data("price") > row.last){
								priceWrap.removeClass("data-up").addClass("data-down");
							}
						}
						$(this).find(".row-buy price font").text(row.buy);
						$(this).find(".row-sell price font").text(row.sell);
						$(this).find(".row-high price font").text(row.hight);
						$(this).find(".row-low price font").text(row.low);
						$(this).find(".row-vol price font").text(row.vol + ($(this).data("type") == "btc" ? "฿" : ($(this).data("type") == "ltc" ? "Ł" : "")));
					}
				});
				
				//重置底部时间
				bottomTime.restart();
			}, "json");
		}, 5000);
		
		bottomTime.start();
	})();
});