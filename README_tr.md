Python version = 3.9.1

### Kurulum

```
python -m venv env
env/Scripts/Activate
pip install requirements.txt
```

### Klasör yapısı
#### Data
- __figures__ -> Raporda kullanılan figürler.

- __info__
    - __synthetic.json__ -> Sentetik resimlerin, pad scorelarını, train veri setindeki iris resimleriyle eşleşme skorlarını, pad ve verieye elemelerini geçip geçmedikleri ve prop_of_i(impostor olma ihtimali) verilerini içerir.
    - __synthetic_with_pairs.json__ -> synthetic.json ile aynı verileri içerir, sadece ekstra olarak iris eşleşme skorlarının hangi train iris resmine ait olduğu bilgisini de içerir.
    - __train.json__ -> Train veri setindeki resimlerin, fold, kimlik, VeriEye tarafından belirlenmiş iris sınır noktaları ve pad score verilerini içerir.
    - __train_pairs.json__ -> Train veri setindeki resimlerin kendi aralarında karşılaştırma skorlarını içerir.

- __synthetic__ -> Tüm foldlarda üretilmiş sentetik iris resimlerini içerir.
    - İsimlendirme: X_Y, X => Fold, Y => Image number

- __train__ -> Eğitim veri setindeki iris resimlerini içerir, resimler kimlik bazında klasörlenmiştir. Sol ve sağ gözler ayrı kimlik olarak alınmıştır.

#### Models
Her folda ait eğitilmiş GAN modellerini içerir.

#### Pad
DNet_Pad algoritmasını ve eğitilmiş modelini içerir. Bu algoritma kullanılarak pad scoreları elde edilir.

#### Notebooklar

- __attack_elimination.ipynb__ -> Sentetik iris resimlerinin impostor olma olasılıklarını hesaplar. Atak eleme işlemlerinin kodlarını içerir. Olasılığı en yüksek 400 tanesi elemeyi geçmiş sayılıyor.

- __attack_experiments.ipynb__ -> Atak deneylerinin sonuç üretim kodlarını içerir.

- __pad_elimination.ipynb__ -> Sentetik resim üretimi ve pad eleme işlemlerinin kodlarını içerir. Normal dağılım içerisinde rastgele bir nokta seçilerek eleme işlemi gerçekleştiriliyor.(Rejection sampling)

- __pad_elimination.ipynb__ -> PAD deneylerinin sonuö üretim kodlarını içerir.

- __prep.ipynb, prepare_dataset.ipynb__ -> Veri hazırlama kodlarını içerir.

- __report.ipynb__ -> Raporlama için gerekli veri ve figürlerin üretilmesi için gerekli kodları içerir.

- __verieye.ipynb__ -> Eş ve eş olmayan irislerin eşleşme skoru dağılımları grafiğinin kodlarını içerir.
-