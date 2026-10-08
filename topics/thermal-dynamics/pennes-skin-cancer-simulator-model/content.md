---
title: "Pennes Skin Cancer Simulator Model"
topic: thermal-dynamics
example: pennes-skin-cancer-simulator-model
status: concept-note
languages: [en, zh-TW, fr, de, ru]
created: 2026-10-08
author: Wei-Che Hung
---

# Pennes Skin Cancer Simulator Model

![Pennes Skin Cancer Simulator Model](media/pennes-skin-cancer-simulator-model.gif)

## What happens

1. A 48 × 48 mm patch of skin is modelled as five layers (epidermis, papillary dermis, reticular dermis, fat, muscle), 11.7 mm down to the body core. A lesion $\Lambda$ , a disc of radius 4.05 mm in the example scene, replaces the tissue properties down to the depth $d = 1.0$ mm. A stimulator pad covers the polygon $\Sigma$ on the surface.
2. Every point of the tissue follows the Pennes heat balance: conduction, heat exchange with blood at 37 °C, and metabolic heat. The blood perfusion is scaled by a smooth random multiplier $m(x,y)$ , so the perfusion varies from place to place. The lesion has about five times the perfusion and ten times the metabolic heat of the reticular dermis.
3. Before the stimulus the skin is at rest, in equilibrium with a 21 °C room above and the 37 °C core below. The lesion is warmer at rest: 34.45 °C against 34.00 °C for normal skin (median surface values).
4. The stimulator adds a heat flux of 206.5 W/m² on $\Sigma$ for 90 s, while convection keeps acting on the whole surface. Heat soaks into the tissue under the pad and spreads sideways past its edge. One step of the model is one camera frame of 1/30 s.
5. The stimulator turns off and the skin recovers for 300 s. Heat keeps spreading sideways and deeper while blood, the room air and the core carry it away. After 300 s the skin is still up to 0.13 °C above rest.
6. The surface temperature is mapped from the 0.4 mm model cells to the 0.2 mm camera pixels, and Gaussian camera noise is added. The result is a noisy recovery video and its noise-free twin.

## Concept

```math
\rho c\,\frac{\partial T}{\partial t} = \nabla\cdot\left(k\,\nabla T\right) + m\,\omega_b\,\rho_b c_b\,(T_b - T) + Q_m
```

Here $\rho c$ is the volumetric heat capacity, $k$ the thermal conductivity, $\omega_b$ the blood perfusion rate, $\rho_b c_b$ and $T_b = 37$ °C the heat capacity and temperature of blood, and $Q_m$ the metabolic heat. The layer and lesion values are taken from Kandala, Deng & Herman (2013). The faces of the tissue block carry

```math
-k\,\frac{\partial T}{\partial z}\Big|_{z=0} = h\,(T_\infty - T_s) + q(t)\,\chi_\Sigma(x,y), \qquad
T\big|_{z=Z} = 37\,{}^{\circ}\mathrm{C}, \qquad
\frac{\partial T}{\partial n} = 0 \ \text{on the sides},
```

with $h = 10$ W/m²K, room temperature $T_\infty = 21$ °C, surface temperature $T_s$ , and the stimulator flux $q(t)$ switched on for the heating time only. The start is the rest state, the steady solution with $q = 0$ .

The block is divided into 120 × 120 cells of 0.4 mm and 55 depth nodes, finest at the surface. One time step equals one camera frame, $\Delta t = 1/30$ s: conduction in depth and the blood term are treated implicitly, sideways conduction explicitly. The camera then records

```math
\mathbf Y_n = U\,\mathbf T_s(t_n) + \boldsymbol\varepsilon_n, \qquad
\varepsilon_n(p) \sim \mathcal N\left(0, \sigma^2\right), \qquad \sigma = 0.05\,{}^{\circ}\mathrm{C},
```

where $U$ is the cell-centred 2× bilinear upsampling to the camera grid. The noisy frames $\mathbf Y_n$ stand in for the camera video, and the noise-free frames $U\,\mathbf T_s(t_n)$ hold the known truth. Features computed from such recovery curves are covered in [PCA Parameter-Difference Features](../pca-parameter-difference-features/content.md) and [Statistical Similitude Features](../statistical-similitude-features/content.md).

## Summary

A 3D Pennes bioheat model of layered skin with a lesion is heated through a pad on the surface and then left to recover, with every model step equal to one camera frame. Its surface temperature becomes a noisy recovery video and a noise-free twin. The twin is the known truth against which each step of a recovery-curve analysis can be checked, which real clinical data cannot provide.

### 繁體中文

一個含病灶的分層皮膚三維 Pennes 生物熱模型，先由表面的加熱片加熱，再讓它自然恢復，模型的每一步都等於相機的一幀。它的表面溫度被寫成一段含雜訊的恢復影片，以及一份無雜訊的對照。這份無雜訊對照就是已知的真值，可以用來檢查恢復曲線分析的每一個步驟，而真實的臨床資料無法提供這一點。

### Français

Un modèle bio-thermique de Pennes en 3D, celui d'une peau en couches avec une lésion, est chauffé par un patch posé sur la surface puis laissé en récupération, chaque pas du modèle valant une image de la caméra. Sa température de surface devient une vidéo de récupération bruitée et un double sans bruit. Ce double est la vérité connue qui permet de vérifier chaque étape d'une analyse des courbes de récupération, ce que les données cliniques réelles ne peuvent pas offrir.

### Deutsch

Ein 3D-Pennes-Biowärmemodell geschichteter Haut mit einer Läsion wird über ein Pad auf der Oberfläche erwärmt und erholt sich danach, wobei jeder Modellschritt genau einem Kamerabild entspricht. Seine Oberflächentemperatur wird zu einem verrauschten Erholungsvideo und einem rauschfreien Zwilling. Der Zwilling ist die bekannte Wahrheit, an der jeder Schritt einer Analyse der Erholungskurven geprüft werden kann – etwas, das echte klinische Daten nicht liefern können.

### Русский

Трёхмерная биотепловая модель Пеннеса для слоистой кожи с очагом поражения нагревается через пластину на поверхности, а затем восстанавливается; каждый шаг модели равен одному кадру камеры. Её поверхностная температура превращается в зашумлённое видео восстановления и его двойника без шума. Этот двойник — известная истина, по которой можно проверить каждый шаг анализа кривых восстановления, чего реальные клинические данные дать не могут.
