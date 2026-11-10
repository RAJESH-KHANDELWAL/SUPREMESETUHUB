"""Textile and craft traditions of Bharat: source-aware regional index."""
TEXTILE_CRAFTS = {
 "bandhani":{"name":"Bandhani / Bandhej","regions":["Gujarat","Rajasthan"],"technique":"Tie-resist dyeing","research":["regional motifs","community artisan histories","natural and synthetic dyes","market change","GI status where applicable"]},
 "patola":{"name":"Patola","regions":["Patan, Gujarat"],"technique":"Double ikat weaving","research":["warp-weft resist planning","Salvi weaving histories","motifs","loom knowledge","artisan transmission"]},
 "kalamkari":{"name":"Kalamkari","regions":["Andhra Pradesh","Telangana"],"technique":"Pen-drawn or block-printed textile traditions","research":["Srikalahasti and Machilipatnam traditions","dye processes","narrative imagery","artisan communities"]},
 "kanjeevaram":{"name":"Kanchipuram silk weaving","regions":["Tamil Nadu"],"technique":"Silk weaving with distinctive borders and motifs","research":["weaving clusters","materials","motif vocabulary","weaver communities","trade and contemporary markets"]},
 "phulkari":{"name":"Phulkari","regions":["Punjab and adjoining regions"],"technique":"Embroidery","research":["women's domestic histories","regional stitches","wedding textiles","partition and migration memories"]},
 "pashmina":{"name":"Pashmina weaving","regions":["Kashmir and Ladakh contexts"],"technique":"Fine animal-fibre textile craft","research":["fibre provenance","spinning","weaving","craft labour","wildlife and legal sourcing"]}
}
def list_textile_crafts():
    return [{"id":key, **value} for key,value in TEXTILE_CRAFTS.items()]
